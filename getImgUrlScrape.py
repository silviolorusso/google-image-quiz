#!/home2/silviolo/python/bin/python 
# -*- coding: utf-8 -*-

# Get first image url from Google query

# MODULES

import urllib2
import random
from bs4 import BeautifulSoup
import re

# FUNCTIONS

def randWord():
	words = []
	f = open("list.txt", "r")
	for line in f:
		# remove /n 
		line = line.rstrip()
		words.append(line)
	rand = random.choice(words)
	return(rand)

def searchScrape(term):
	headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0' }
	searchUrl = "http://google.com/images?source=hp&q=" + term
	req = urllib2.Request(searchUrl, None, headers)
	html = urllib2.urlopen(req).read()
	soup = BeautifulSoup(html)
	links = soup.findAll("a", { "class" : "rg_l" })
	messyLink = links[0].get("href")
	imgUrl = re.search( r'imgurl=(.*)&imgrefurl', messyLink).groups()[0]
	# check if it's a broken link
	class HeadRequest(urllib2.Request):
		def get_method(self):
			return "HEAD"
	try:
		response = urllib2.urlopen(HeadRequest(imgUrl))
	except:
		print('Error: forbidden!')
		return
	# reverse the query
	rterm = term[::-1]
	print(rterm + ' ' + imgUrl)
	return([rterm, imgUrl])

# TEST

if __name__ == "__main__":
	searchScrape(randWord())
