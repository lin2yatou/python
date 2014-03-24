#!/usr/bin/python
# Filename: httpclient.py

import os
import sys
import httplib as hl

class httpclient:
    '''This is a sealed http poster.

    Use this class to send http request.'''

    def __init__(self, url, method, header, content):
        self.url = url
        self.method = method
        self.header = header
        self.content = content

    def __init__(self):
        pass

    def gethostofurl(self, url):
        url = url.lstrip("htp:/ ")
        firstslashinurl = url.find('/')
        if firstslashinurl == -1:
            host = url[0:]
        else:
            host = url[0:firstslashinurl]
        return host

    def dopost(self, host, url, header, content):
        #TODO: implement do post method
        pass

    def doget(self, host, url, header, content):
        #TODO: implement do get method
        conn = hl.HTTPConnction(host)
        conn.request('GET', url, content, header)
        resp = conn.getresponse()
        return resp

    def dorequest(self, url, method, header, content):
        #TODO: implement
        host = gethostofurl(url)
        if method.lower() == 'get':
            return doget(host, url, header, content)
        elif method.lower() == 'post':
            return dopost(url, header, content)
 

hc = httpclient()
if len(sys.argv) >= 2:
    print hc.gethostofurl(sys.argv[1])

