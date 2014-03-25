#!/usr/bin/python
# Filename: httpclient.py

import sys
import os
import httplib
import urllib

class httpclient:
    JWAPIURL = "api.jingwei.com"

    # use a URL with port number if need to specify a port, by default is 80
    # Example: http://www.foo.org:8080/hello/iamhere.html
    def __init__(self, url):
        self.url = url
        self.host = self.gethostofurl(url)
        self.port = self.getportofurl(url)
        pass

    def buildbody(self, content):
        # if the content is raw string, pass it to the request
        # else, if it's a dictionary, build the request body.
        if content and isinstance(content, dict):
            body = urllib.urlencode(content)
            return body

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

    # The content could be a String, or a dictionary, the buildbody method will convert the map to a string with URL encoding.
    # The header should be a map type, or it will be ignore.
    def dorequest(self, method='get', content=None, header=None):
        method = method.upper()
        body = self.buildbody(content)
        conn = httplib.HTTPConnection(self.host, self.port)
        if header and isinstance(header, map):
            conn.request(method, self.url, body, header)
        else:
            conn.request(method, self.url, body)
        
        resp = conn.getresponse()
        return resp
        
if __name__ == '__main__': 
    hc = httpclient('http://www.douban.com/')
    resp = hc.dorequest()
    print resp.read()
