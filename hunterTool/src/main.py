#!/usr/bin/python
# -*- coding: utf-8 -*-
from github import Github

def __unicode__(self):
    return unicode(self.user)

def showRepoByKeyword(gita, keyword):
#    rs=gita.search_repositories(keyword,language='javascript')
    rs=gita.search_repositories(keyword,language='javascript',pushed=">=2015-06-30")

    limit = 1
    for repo in rs:
        print(repo.name+" "+repo.language)
        print(repo.owner)
        limit += 1
        if limit > 15:
            break


if __name__ == '__main__' :
    print("username:")
    username = raw_input()
    print("password:")
    password = raw_input()
    gita = Github(username, password)
    showRepoByKeyword(gita, "node.js")


# Then play with your Github objects:
#for repo in g.get_user().get_repos():
#    print repo.name
