#!/usr/bin/python
# Filename: httpclient.py

import sys
import os
import httplib
import urllib

class httpclient:
    JWAPIURL = "api.jingwei.com"

    def __init__(self, host=JWAPIURL, port='80'):
        self.host = host
        self.port = port
        pass

    def buildbody(self, content):
        return urllib.urlencode(content)

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

    def dorequest(self, method, url, content, header):
        # If the host / port had been initialized, use the default value.
        if not self.host:
            self.host = self.gethostofurl(url)
        if not self.port:
            self.port = self.getportofurl(url)
        if method.lower() == 'get':
            method = 'GET'
        elif method.lower() == 'post':
            method = 'POST'

        # if the content is raw string, pass it to the request
        # else, if it's a dictionary, build the request body.
        body = content 
        if isinstance(content, dict):
            body = urllib.urlencode(content)

        print self.host + ':' + self.port
        conn = httplib.HTTPConnection(self.host, self.port)

        if isinstance(header, dict):
            conn.request(method, url, body, header)
        else:
            conn.request(method, url, body)
        
        resp = conn.getresponse()
        return resp
        
if __name__ == '__main__' and len(sys.argv) >= 2:
    hc = httpclient()
    resp = hc.dorequest('get', 'http://www.douban.com/', None, '')
    #print resp.read()
