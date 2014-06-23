#!/usr/bin/env 
# -*- coding: utf-8 -*-

# Get first image url from Google query

# MODULES

import urllib2
import simplejson
import random

# VARIABLES

searchTerm = 'parrot'

# FUNCTIONS

def getWord():
	words = []
	f = open("list.txt", "r")
	for line in f:
		# remove /n 
		line = line.rstrip()
		words.append(line)
		rand = random.choice(words)
	return(rand)

def search():
	term = getWord()
	fetcher = urllib2.build_opener()
	searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + term
	f = fetcher.open(searchUrl)
	imgs = simplejson.load(f)
	# check if a result exists
	try:
		imgUrl = imgs['responseData']['results'][0]['unescapedUrl']
		# check if it's a broken link
		class HeadRequest(urllib2.Request):
			def get_method(self):
				return "HEAD"
		try:
			response = urllib2.urlopen(HeadRequest(imgUrl))
		except:
			print('Error: forbidden!')
			search()
		# reverse the query
		rterm = term[::-1]
		print(rterm + ' ' + imgUrl)
		return([rterm, imgUrl])
	except IndexError:
		print('Error: no images found!')
		search()

# TEST

if __name__ == "__main__":
	search()