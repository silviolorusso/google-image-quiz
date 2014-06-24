#!/home2/silviolo/python/bin/python 
# -*- coding: utf-8 -*-

# Create Db with query, image url

# MODULES

import sqlite3
import urllib2
import simplejson
from getImgUrl import search
from time import sleep

# FUNCTIONS

def getWords():
	words = []
	f = open("list.txt", "r")
	for line in f:
		# remove /n 
		line = line.rstrip()
		words.append(line)
	return words

# WORK

words = getWords()

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
    		print('Error!')
    		pass
    	sleep(3)