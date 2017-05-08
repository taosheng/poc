#!/usr/bin/env python


import ldap, ldif
from ldap.controls import SimplePagedResultsControl
import sys
import ldap.modlist as modlist
import getpass
import csv
from cStringIO import StringIO
from mrjob.job import MRJob


# Generate personal web behavior report from apache log...
# assume all the access log was aggregated.
# usage #./mrWebPersonalReport.py --cleanup NONE 20150525_all_log.csv
#

class MRTboxWebReport(MRJob):

    def configure_options(self):
        super(MRTboxWebReport, self).configure_options()

    def mapper_filter(self, _, line):
        aline = StringIO(line)
        for rows in csv.reader(aline, delimiter=' '):
            if rows[11].startswith('Mozilla') and rows[4] != '-':
                action = rows[7].split("?")[0]
                action = action.replace("HTTP/1.","")
                if action.startswith("GET /I/"):
                    action ="View Image On Brower"
                if "." in action:
                    action = "File Action:" + action
                yield (rows[4],rows[5]), [ int(rows[1])/1000000.0, action]


   # def combiner_check_exists(self, key, values):
        #print "lala"+ key
  #      existUser = 'None'
  #      key = key.replace('"','')
  #      try:
  #          existUser = str(getUser(key))
  #      except:
  #          existUser = 'None'
#
#        if (existUser == 'None'):
#            for v in values:
#                yield key+"@"+v[7].split("?")[0], 1

    def reducer(self, key, values):
        for v in values:
            yield key, v
    

    def steps(self):
        return [
            self.mr(mapper=self.mapper_filter,
                   # combiner=self.combiner_check_exists,
                    reducer=self.reducer)
        ]



#    print str(getUser("jerry_yang"))
if __name__ == '__main__':
    ajob = MRTboxWebReport(args=['--cleanup','NONE'])
    ajob.run()


