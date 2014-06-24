#!/home2/silviolo/python/bin/python 
# -*- coding: utf-8 -*-

# Create Db with query, image url

# MODULES

import sqlite3
import urllib2
import simplejson
from time import sleep

# FUNCTIONS

def getWord():
	words = []
	f = open("list.txt", "r")
	for line in f:
		# remove /n 
		line = line.rstrip()
		words.append(line)
	return words

def search(term):
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
		return

# WORK

words = getWord()

# create / connect to db
conn = sqlite3.connect(r"./queries.db")

with conn:
    cur = conn.cursor()
    # drop Queries
    try:
    	cur.execute('''DROP TABLE Queries''')
    except:
    	pass
    # create Queries
    try:
    	cur.execute("CREATE TABLE Queries(Id INT, Query TEXT, Url TEXT)")
    except:
    	pass
    i = 0
    for word in words:
    	try:
    		output = search(word)
    		cur.execute("INSERT INTO Queries VALUES(?,?,?)", (i, output[0], output[1]))
    		conn.commit()
    		i += 1
    	except:
    		print('Error')
    		sleep(10)
    		pass
    	sleep(3)

# with conn:
#     cur = conn.cursor()
#     # drop Queries
#     try:
#     	cur.execute('''DROP TABLE Queries''')
#     except:
#     	pass
#     # create Queries
#     try:
#     	cur.execute("CREATE TABLE Queries(Id INT, Query TEXT, Url TEXT)")
#     except:
#     	pass
#     i = 0
#     for word in words:
#     	try:
#     		output = search(word)
#     		print output[0]
#     		print output[1]
#     		imgUrl = output[1]
#     		# check if it's a broken link
#     		class HeadRequest(urllib2.Request):
#     			def get_method(self):
#     				return "HEAD"
# 				try:
# 					response = urllib2.urlopen(HeadRequest(imgUrl))
# 				except:
# 					pass
# 				cur.execute("INSERT INTO Queries VALUES(?,?,?)", (i, output[0], output[1]))
# 				conn.commit()
# 				i += 1
#     	except:
#     		print('Error')
#     		sleep(10)
#     		pass
#     	sleep(3)