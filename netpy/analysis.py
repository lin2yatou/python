#!/usr/bin/python
# Filename: analysis.py
# author: linnan
# history: 2014-06-09 17:06:50
import json
import urllib2
import netcore
class user:
	def __init__(self, userid):
		self.id=userid
		self.nc=netcore.netcore("http://yun.baidu.com/")

	def getfans(self):
		return json.loads(self.nc.get("pcloud/friend/getfanslist?query_uk=1543772036&limit=24&start=0&bdstoken=435c080ac4fcf05ac51de7cb37dc7709&channel=chunlei&clienttype=0&web=1"))

	def getfollows(self):
		return json.loads(self.nc.get("pcloud/friend/getfollowlist?query_uk="+self.id+"&limit=24&start=0&bdstoken=435c080ac4fcf05ac51de7cb37dc7709&channel=chunlei&clienttype=0&web=1"))

	def getshares(self):
		return json.loads(self.nc.get("pcloud/feed/getsharelist?t=1401961615134&category=0&auth_type=1&request_location=share_home&start=0&limit=60&query_uk=1543772036&channel=chunlei&clienttype=0&web=1&bdstoken=435c080ac4fcf05ac51de7cb37dc7709"))

if __name__ == "__main__":
	me=user("1543772036")
	print me.getfans()
	#print me.getfollows()
	#print me.getshares()
