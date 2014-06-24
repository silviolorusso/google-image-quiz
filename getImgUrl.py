#!/home2/silviolo/python/bin/python 
# -*- coding: utf-8 -*-

# Get first image url from Google query

# MODULES

import urllib2
import simplejson
import random

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

def search(term):
	fetcher = urllib2.build_opener()
	fetcher.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36')]
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
	except TypeError:
		print('Error: no images found!')
		return

# TEST

if __name__ == "__main__":
	search(randWord())
