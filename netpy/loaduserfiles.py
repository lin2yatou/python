#!/usr/bin/python
# Filename: loaduserfiles.py
# author: administrator
# history: 2014-06-13 14:24:40

import urllib2
import json
import netcore
import analysis
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   

def getallshare(uid):
    u = analysis.user(uid)
    contentsArr = []
    limit = 60
    got = 0
    start = 0
    shares = u.getshares()
    total = shares.get("total_count")

    while(got<total):
        if(shares and shares.get("records")):
            for rec in shares.get("records"):
                uk = rec.get("uk")
                shareid = rec.get("shareid")
                if(rec and rec.get("filelist")):
                    for file in rec.get("filelist"):
                        if file.get("isdir") == 0:
                            contentsArr = contentsArr + [(\
                            file.get("server_filename"),\
                            file.get("size"),\
                            file.get("md5"),\
                            uk,\
                            shareid,\
                            file.get("fs_id"))\
                            ]
                        if file.get("isdir"):
                            path = file.get("path")
                            contentsArr = contentsArr + getfilesinfolder(u,path,shareid,uk)
        if not shares.get("records"):
            break
        got += 60
        start += 1
        shares=u.getshares(start)
    return contentsArr



def getfilesinfolder(u,path,shareid,uk):
    lists = u.listfolder(path,shareid,uk)
    index = 1
    contentsArr = []
    if not lists:
        return contentsArr
    while(lists and lists.get("list")):
        for li in lists.get("list"):
            if li.get("isdir") == 0:
                contentsArr = contentsArr + [(\
                li.get("server_filename"),\
                li.get("size"),\
                li.get("md5"),\
                uk,\
                shareid,\
                li.get("fs_id"))\
                ]
            if li.get("isdir"):
                p = li.get("path")
                contentsArr = contentsArr + getfilesinfolder(u,p,shareid,uk)
        index +=1
        lists = u.listfolder(path, shareid, uk, index)
    return contentsArr

def getfollows(uid):
    u = analysis.user(uid)
    follows = u.getfollows()
    followArr = []
    if(follows and follows.get("follow_list")):
        for follow in follows.get("follow_list"):
            followArr.extend([(\
            follow.get("follow_uname"),\
            follow.get("follow_uk"),\
            follow.get("follow_count"),\
            follow.get("fans_count"))\
            ])
    return followArr

def getfans(uid):
    u = analysis.user(uid)
    print "getting fans of user: " + uid
    fans = u.getfans()
    fanArr = []
    if(fans and fans.get("fans_list")):
        for fan in fans.get("fans_list"):
            fanArr.extend([(\
            fan.get("fans_uname"),\
            fan.get("fans_uk"),\
            fan.get("follow_count"),\
            fan.get("fans_count"))\
            ])
    return fanArr


if __name__ == "__main__":
    allshare = getfans("1543772036")
    for share in allshare:
        for obj in share:
            print obj
