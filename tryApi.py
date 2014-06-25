#!/usr/bin/env 
# -*- coding: utf-8 -*-

# MODULES

import web
from getImgUrl import search
from getImgUrlDb import searchDb
from time import sleep

# WORK

while True:
	term = search(randWord())
	try:
		print term[0]
		print term[1]
	except:
	 	term = searchDb()
		print("db!")
		print term[0]
		print term[1]
	sleep(0.5)