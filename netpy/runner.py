#!/usr/bin/python
# Filename: runner.py
# author: administrator
# history: 2014-06-13 16:08:08
import urllib2
import json
import netcore as net
import dbcore as db
import analysis as ana
import sys
import loaduserfiles as lo

reload(sys)
sys.setdefaultencoding('utf8')
def start():
    while True:
        try:
            u = db.readuser()
            if u != None and u != 0:
                uid = u[1]
                storefans(uid)
                storefollows(uid)
                storefiles(uid)
            else:
                break;
        except Exception,e:
            print e
        move2parsed(u)
        

def storefiles(uid):
    allshares = lo.getallshare(uid)
    for share in allshares:
        db.insertfile(share[0], share[1], share[2], share[3], share[4], share[5])

def storefans(uid):
    fansArr = lo.getfans(uid)
    for fans in fansArr:
        if not db.isparseduser(fans[1]):
            db.insertuser(fans[0],fans[1],fans[2],fans[3])

def storefollows(uid):
    followArr = lo.getfollows(uid)
    for follow in followArr:
        id = follow[1]
        if not db.isparseduser(id):
            db.insertuser(follow[0],follow[1],follow[2],follow[3])

def move2parsed(userinfo):
    uid = userinfo[1]
    db.insertparseduser(userinfo[0],userinfo[1],userinfo[2],userinfo[3])
    db.deleteuser(uid)


if __name__ == "__main__":
    start()
