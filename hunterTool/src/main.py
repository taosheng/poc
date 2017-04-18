#!/usr/bin/python
# -*- coding: utf-8 -*-
from github import Github
import sys

def showUserInfo(namedUser):
    info = u''
#    info = info + namedUser.name.encode('utf-8') + " "
    info = info + str(namedUser.email) +", "
    try:
        location = namedUser.location.decode('UTF-8')
        info = info+'"' + location + '", '
    except:
        info = info +"<location encoding>, "
#    info = info + "cont:"+str(namedUser.contributions) + ", "
#    info = info + "name:"+str(namedUser.name) + ", "
    info = info + "personal_web:"+str(namedUser.blog) + ", "
    info = info + "giturl:"+str(namedUser.html_url) + ", "
    info = info + "prepo:"+str(namedUser.public_repos) + ", "
#    info = info + "repo:"+str(namedUser.get_repos) + ", "
#    info = info + "watch:"+str(namedUser.get_watched) + ", "
#    info = info + "starred:"+str(namedUser.get_starred) + ", "
    info = info + "following:"+str(namedUser.following) + ", "
    info = info + "follower:"+str(namedUser.followers) + ", "

    return info


def showUsers(gita):
    us = gita.search_users('language:javascript location:taiwan')
    #us = gita.search_users('language:javascript',lauguage='javascript',location='taiwan')
    limit = 1
    for u in us:
        if u.email is None:
            continue
        print(showUserInfo(u))
        limit += 1
        if limit >= 200: 
            break

def showRepoByKeyword(gita, keyword):
#    rs=gita.search_repositories(keyword,language='javascript')
    rs = gita.search_repositories(keyword,language='javascript',pushed=">=2015-06-30")

    rlimit = 1
    for repo in rs:
        if repo.owner.email is None:
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
#    print("username:")
#    username = raw_input()
#    print("password:")
#    password = raw_input()
    gita = Github(sys.argv[1],sys.argv[2])
    #showRepoByKeyword(gita, "node.js api")
    showUsers(gita)


# Then play with your Github objects:
#for repo in g.get_user().get_repos():
#    print repo.name
