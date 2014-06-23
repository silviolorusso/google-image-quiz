#!/usr/bin/env 
# -*- coding: utf-8 -*-

# MODULES

import web
from getImgUrl import search
from time import sleep



while True:
	term = search()
	print term[0]
	print term[1]