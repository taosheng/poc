#!/usr/bin/python
# -*- coding: utf-8 -*-
from github import Github
import sys
import pprint
import datetime

def getUserPushEventsNo(namedUser, daysBefore):
    events = namedUser.get_events()
    pp = pprint.PrettyPrinter(indent=4)
    cnt = 0
    bef = datetime.datetime.now() - datetime.timedelta(days=daysBefore)
    for e in events:
        if e.type == 'PushEvent' and e.created_at > bef:
            cnt += 1
      #  pp.pprint(e.payload)
    return cnt

def showUserInfo(namedUser):
    info = u''
    info = info + str(namedUser.email) +"; "
    try:
        location = namedUser.location.decode('UTF-8')
        info = info+'"' + location + '"; '
    except:
        info = info +"<encoding issue>; "
#    info = info + "cont:"+str(namedUser.contributions) + ", "
#    info = info + "name:"+str(namedUser.name) + ", "
    try:
        info = info + "personal_web: "+str(namedUser.blog) + "; "
    except:
        info = info + "personal_web: <encoding issue>" + "; "
    info = info + "giturl: "+str(namedUser.html_url) + "; "
    info = info + "prepo:"+str(namedUser.public_repos) + "; "
    info = info + "following:"+str(namedUser.following) + "; "
    info = info + "follower:"+str(namedUser.followers) + "; "

    return info


def showUsers(gita, q):
    us = gita.search_users(q)
    #us = gita.search_users('language:javascript',lauguage='javascript',location='taiwan')
    limit = 1
    for u in us:
        if u.email is None and u.blog is None:
            continue
        print(showUserInfo(u))
#        print(showUserInfo(u)+" work:"+ str(getUserPushEventsNo(u,365)))
#        limit += 1
#        if limit >= 5: 
#            break
#    print(limit)

def showRepoByKeyword(gita, keyword):
#    rs=gita.search_repositories(keyword,language='javascript')
    rs = gita.search_repositories(keyword,pushed=">=2015-06-30")

    rlimit = 1
    for repo in rs:
        if repo.owner.email is None or repo.owner.location is None:
            continue
        if 'Taiwan' not in repo.owner.location :
            continue
   
        print("======================")
        print(repo.name+" "+repo.language)
        print(showUserInfo(repo.owner))
        print("-----contributors ---- ")
        contributors = repo.get_contributors()
        limit = 1

        for cont in contributors:
            if cont.email is None or cont.location is None: 
                continue     
            if 'Taiwan' not in cont.location:
                continue
            print(showUserInfo(cont))
            limit += 1
            if limit > 10:
                print(" ...ignore > 10")
                break

        rlimit +=1
        if rlimit >15:
                break


if __name__ == '__main__' :
    #gita = Github(sys.argv[1],sys.argv[2])
    gita = Github(sys.argv[1]) #token
    keyword = sys.argv[2]
    #showRepoByKeyword(gita, "topic:"+keyword)
    showUsers(gita, 'language:'+keyword+' location:taiwan')
    #showUsers(gita, ' location:taiwan')
    #showUsers(gita, 'dougchen language:python')

