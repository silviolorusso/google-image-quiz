#!/home2/silviolo/python/bin/python 
# -*- coding: utf-8 -*-

# Create Db with query, image url

# MODULES

import sqlite3
import urllib2
from getImgUrlScrape import searchScrape
from time import sleep
import os, shutil
import random

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

# get to script dir, for the cron job
os.chdir(os.path.dirname(os.path.realpath(__file__)))

words = getWords()

# get random sample, otherwise takes ages to build the db. 1200 because some queries fail
rand_smpl = [ words[i] for i in sorted(random.sample(xrange(len(words)), 1200)) ]

# create / connect to db
conn = sqlite3.connect(r"./queries-temp.db")

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
    for word in rand_smpl:
    	try:
    		output = searchScrape(word)
    		cur.execute("INSERT INTO Queries VALUES(?,?,?)", (i, output[0], output[1]))
    		conn.commit()
    		i += 1
    	except:
    		print('Error!')
    		pass
    	sleep(1)

# copy to actual db
shutil.copy2('./queries-temp.db', './queries.db')

# done
print("Database updated.")