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
    def getportofurl(self, url):
        url = url.lstrip('htp:/')
        indexofcolon = url.find(':')
        if indexofcolon > 0:
            indexofslash = url.find('/', indexofcolon)
            return url[indexofcolon + 1:indexofslash]
        else:
            return 80

    def doget(self, url, content, header):
        host = self.gethostofurl(url)
        port = self.getportofurl(url)
        body = urllib.urlencode(content)
        conn = httplib.HTTPConnection(host, port)
        conn.request('GET', url, body, header)
        resp = conn.getresponse()
        return resp

    def dopost(self, url, content, header):
        host = self.gethostofurl(url)
        port = self.getportofurl(url)
        body = urllib.urlencode(content)
        conn = httplib.HTTPConnection(host, port)
        conn.request('POST', url, body, header)
        resp = conn.getresponse()
        return resp

        
if len(sys.argv) >= 2:
    hc = httpclient('')
    print hc.buildbody({'name':'nanan','age':'27'})
    resp = hc.doget('http://www.douban.com/','','')
    #print resp.read()
        
