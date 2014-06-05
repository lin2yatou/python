#!/usr/bin/python
# Filename: netcore.py
# author: linnan
# history: 2014-06-05 13:43:43
import urllib2

class netcore:
	def __init__(self, url):
		self.url=url

	def showUrl(self):
		print "url: "+self.url

	def get(self):
		req = urllib2.Request(self.url)
		resp = urllib2.urlopen(req)
		return resp.read()

	def post(self, data):
		req = urllib2.Request(self.url)
		req.add_data(data)
		resp = urllib2.urlopen(req)
		return resp.read()

nc = netcore("http://www.jingwei.com/")
nc.showUrl()
print nc.get()
