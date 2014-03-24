#! /user/bin/python

import sys
import httplib
import simplejson
import hashlib

username = raw_input('Input your username:')
key = 'a92a32bcbae61c4f09da0eff0ff66acd6dba'
secret = hashlib.md5('86+'+str(username)+key).hexdigest()
verifycode = ""

url = 'http://mobilepre.jingwei.com/register/register?username=86%2B'+username+'&secret='+secret
header = {'user-agent':'Apache-HttpClient/4.2.1 (java 1.5)','Host':' mobilepre.jingwei.com'}
print "request: "+url
conn = httplib.HTTPConnection("mobilepre.jingwei.com")
conn.request('POST',url,'',header)
res = conn.getresponse()

body = res.read()
print "response: " + body
contiune = 0
register_res = simplejson.loads(body)
if register_res['status'] == 0:
    data = register_res['data']
    verifycode = data['verifyCode']
    print ""
    print "**VerifyCode** : "+ verifycode
    print ""
else:
    print ""
    print "**Message** : " + register_res['message'] 
    print ""
