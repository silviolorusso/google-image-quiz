#!/home2/silviolo/python/bin/python 
# -*- coding: utf-8 -*-

# Create Db with query, image url

# MODULES

import sqlite3
import random

# FUNCTIONS

def searchDb():
	# create / connect to db
	conn = sqlite3.connect(r"./queries.db")
	with conn:
		cur = conn.cursor()
		cur.execute("SELECT * FROM Queries")
		rows = cur.fetchall()
		return([rows[0][1],rows[0][2]])

# TEST

if __name__ == "__main__":
	print(searchDb())