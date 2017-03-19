'''
Created on 2011/7/24

@author: Rad
'''
import threading
import time
import os
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

data_lock = threading.Lock()
cached_data = {}
OP = 'op'
UPDATE_TIME = 'update_time'
SPERATOR = ';'
EXPIRE_TIME = 3600

class MainPage(webapp.RequestHandler):
    def post(self):
        data_id = self.request.get('id')
        op = self.request.get('op')
        print 'POST id=%s, op=%s' % (data_id, op)
        return_data = '==='
        data_lock.acquire()
        try:
            if data_id in cached_data:
                cached_command = cached_data[data_id][OP]
                cached_data[data_id][OP] = (cached_command + SPERATOR + op) if cached_command else op
                cached_data[data_id][UPDATE_TIME] = time.time()
                return_data = cached_data[data_id][OP]
        finally:
            data_lock.release()
        self.response.out.write('<div id="content">' + return_data + '</div>')
    
    def get(self):
        data_id = self.request.get('id')
        if data_id:
            data_lock.acquire()
            try:
                if data_id not in cached_data:
                    cached_data[data_id] = {OP: '', UPDATE_TIME: time.time()}
            finally:
                data_lock.release()
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, {}))

class OpPage(webapp.RequestHandler):
    def get(self):
        data_id = self.request.get('id')
        return_data = 'Wrong id'
        data_lock.acquire()
        try:
            if data_id in cached_data:
                return_data = cached_data[data_id][OP]
                cached_data[data_id][OP] = ''
                cached_data[data_id][UPDATE_TIME] = time.time()
        finally:
            data_lock.release()
        self.response.out.write(return_data)
    
class SecurePage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            now = time.time()
            data_lock.acquire()
            try:
                for data_id, data in cached_data:
                    if now - data[UPDATE_TIME] > EXPIRE_TIME:
                        del cached_data[data_id]
            finally:
                data_lock.release()
            self.response.out.write(
                'Hello %s <a href="%s">Sign out</a><br>Is administrator: %s' % 
                (user.nickname(), users.create_logout_url("/"), users.is_current_user_admin())
            )
        else:
            self.redirect(users.create_login_url(self.request.uri))

application = webapp.WSGIApplication([('/', MainPage),
                                      ('/op', OpPage),
                                      ('/se', SecurePage)], debug=True)


def main():
    run_wsgi_app(application)


if __name__ == "__main__":
    main()