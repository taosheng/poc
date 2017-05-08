#!/usr/bin/env python3
from ldap3 import Server, Connection, ALL
import pprint
import sys
import getpass
import time
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import LogisticRegressionModel,SVMModel,SVMWithSGD
from pyspark.mllib.linalg import SparseVector

""" This is a simple tool to build AD Groups to SparseVector
    See pyspark.mllib
    See ldap3
"""
_GROUPLIST = [] #TODO Improve

def getSVfromGroup(glist):
    """ SparseVector default value should be 1.0 if existing """
    v=[]
    for g in glist:
        idx = getIdxGroup(g)
        if idx > 0:
            v.append(idx)

    vs = {}
    for i in v:
        vs[i] = 1.0

    return SparseVector(len(_GROUPLIST), vs)


def getIdxGroup(groupname):
    
    if groupname in _GROUPLIST: 
        return _GROUPLIST.index(groupname) + 1
    else:
        return 0
    
def getGroupsFromAd():

    AD_BASE = 'DC=tw,DC=trendnet,DC=org'
    AD_FILTER = '(objectClass=group)'

    hugeGroupList = []
    try:
        server = Server(SERVER, get_info=ALL)
        conn = Connection(SERVER, user=AD_LOGIN, password=SECRET, auto_bind=True)
        results = conn.extend.standard.paged_search(AD_BASE,AD_FILTER, paged_size=200)
        cnt = 0
      
        for r in results:
            if 'dn' in r:
                cnt+= 1
                hugeGroupList.append(str(r['dn']))
          

        return hugeGroupList # TODO 


    except Exception as e:
        sys.stderr.write('Error connecting to LDAP server: \n'+str(e)+"\n\n")
        sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 4 :
        print("Usage: python3 buildGroupSV.py <AD IP> <Login_name> <password> ")
        print("this is a simple utility used in your program, run directly is just for testing\n")
 
        sys.exit(0)

    SERVER = sys.argv[1]
    AD_LOGIN = sys.argv[2]
    SECRET = sys.argv[3]


    _GROUPLIST = getGroupsFromAd()

    print(getIdxGroup('CN=TW User Account Modify Admin,OU=AD Privilege Groups,DC=tw,DC=trendnet,DC=org'))
    print(getSVfromGroup(['CN=TW User Account Modify Admin,OU=AD Privilege Groups,DC=tw,DC=trendnet,DC=org','CN=All of TW SafeSync for Enterprise, DC=tw,DC=trendnet,DC=org']))
