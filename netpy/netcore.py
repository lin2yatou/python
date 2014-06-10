#!/usr/bin/python
# Filename: netcore.py
# author: linnan
# history: 2014-06-05 13:43:43
import urllib2
import json

class netcore:
	def __init__(self, host):
		self.host=host

	def get(self, path=""):
		req = urllib2.Request(self.host+path)
		resp = urllib2.urlopen(req)
		return resp.read()

	def post(self, path='', data=''):
		req = urllib2.Request(self.host+path)
		req.add_data(data)
		resp = urllib2.urlopen(req)
		return resp.read()

if __name__ == "__main__":
	nc = netcore("http://www.jingwei.com/")
	print nc.post()

