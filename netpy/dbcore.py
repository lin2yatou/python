#!/usr/bin/python
# Filename: dbcore.py
# author: administrator
# history: 2014-06-10 10:33:36

import MySQLdb as mysql

def insertuser(username, userid, followcount, fanscount):
    try:
        conn = mysql.connect(host='localhost',user='root',passwd='password',db='yunpandb', charset='utf8')
        cur = conn.cursor()
        count = cur.execute('insert into users values (%s, %s, %s, %s)', [username, userid, followcount, fanscount])
        conn.commit()
        cur.close()
        conn.close()
    except mysql.Error,e:
        print "Mysql error: %d: %s" % (e.args[0], e.args[1])
        return 0
    return count

def readuser():
    try:
        conn = mysql.connect(host='localhost',user='root',passwd='password',db='yunpandb', charset='utf8')
        cur = conn.cursor();
        cur.execute("select username, userid, followcount, fanscount from users")
        result = cur.fetchone()
        cur.close()
        conn.close()
    except mysql.Error,e:
        print "Mysql error: %d: %s" % (e.args[0], e.args[1])
        return 0
    return result

def deleteuser(userid):
    try:
        conn = mysql.connect(host='localhost',user='root',passwd='password',db='yunpandb', charset='utf8')
        cur = conn.cursor()
        count = cur.execute("delete from users where userid = %s", userid)
        conn.commit()
        cur.close()
        conn.close()
    except mysql.Error, e:
        print "Mysql error: %d: %s" % (e.args[0], e.args[1])
    return count

#insertuser('abc', '123', 4, 5)
#delete1user(123)

def insertparseduser(uname, uid, followcount, fanscount):
    try:
        count = 0
        conn = mysql.connect(host='localhost',user='root',passwd='password',db='yunpandb', charset='utf8')
        cur = conn.cursor()
        count = cur.execute('insert into user_parsed values (%s, %s, %s, %s)', [uname, uid, followcount, fanscount])
        conn.commit()
        cur.close()
        conn.close()
    except mysql.Error,e:
        print "Mysql error: %d: %s" % (e.args[0], e.args[1])
    return count


def isparseduser(uid):
    try:
        conn = mysql.connect(host='localhost',user='root',passwd='password',db='yunpandb', charset='utf8')
        cur = conn.cursor();
        cur.execute("select username, userid, followcount, fanscount from user_parsed where userid='" + str(uid) + "'")
        result = cur.fetchone()
        cur.close()
        conn.close()
    except mysql.Error,e:
        print "Mysql error: %d: %s" % (e.args[0], e.args[1])
    return result

def readparseduser():
    try:
        conn = mysql.connect(host='localhost',user='root',passwd='password',db='yunpandb', charset='utf8')
        cur = conn.cursor();
        cur.execute("select username, userid, followcount, fanscount from user_parsed")
        result = cur.fetchone()
        cur.close()
        conn.close()
    except mysql.Error,e:
        print "Mysql error: %d: %s" % (e.args[0], e.args[1])
    return result

def deleteparseduser(userid):
    try:
        conn = mysql.connect(host='localhost',user='root',passwd='password',db='yunpandb', charset='utf8')
        cur = conn.cursor()
        count = cur.execute("delete from user_parsed where userid = %s", userid)
        conn.commit()
        cur.close()
        conn.close()
    except mysql.Error, e:
        print "Mysql error: %d: %s" % (e.args[0], e.args[1])
    return count

def insertfile(name, size, md5, uk, shareid, fsid):
    try:
        conn = mysql.connect(host='localhost',user='root',passwd='password',db='yunpandb', charset='utf8')
        cur = conn.cursor()
        count = cur.execute('insert into files values (%s, %s, %s, %s, %s, %s)', [name,size,md5,uk,shareid,fsid])
        conn.commit()
        cur.close()
        conn.close()
    except mysql.Error,e:
        print "Mysql error: %d: %s" % (e.args[0], e.args[1])

def readfile():
    pass

def deletefile():
    pass
