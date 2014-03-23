#!/usr/bin/python
# Filename: httpclient.py

import sys
import os
import httplib
import urllib

class httpclient:
    def __init__(self):
        pass
        
    def __init__(self, host, port='80'):
        pass

    def buildbody(self, content):
        return urllib.urlencde(content)

    def gethostofurl(self, url):
        url = url.lstrip('htp:/')
        slashindexinurl = url.find('/')
        if slashindexinurl != -1:
            host = url[0:slashindexinurl]
        else:
            host = url[0:]
        # remove post number if exists
        if host.find(':') > 0:
            host = host[0:host.find(':')]
        return host
    
    def doget(self, url, content, header):
        host = self.gethostofurl(url)
        port = '80' #TODO: Get the real port num.
        conn = httplib.HTTPConnection(host, port)
        conn.request('GET', url)
        resp = conn.getresponse()
        return resp

    def dopost(self, url, content, header):
        host = self.gethostofurl(url)
        port = '80' #TODO: Get the real port num.
        conn = httplib.HTTPConnection(host, port)
        conn.request('POST', url)
        resp = conn.getresponse()
        return resp

        
if len(sys.argv) >= 2:
    hc = httpclient('')
    print hc.buildbody({'name':'nanan','age':'27'})
    resp = hc.doget('http://www.douban.com/','','')
    #print resp.read()
        
