#!/home2/silviolo/python/bin/python 
# -*- coding: utf-8 -*-

# MODULES

import web
from getImgUrl import search

render = web.template.render('templates/')

urls = (
  '/', 'index'
)

class index:
	def GET(self):
		term = search()
		return render.index(term[0], term[1])

if __name__ == "__main__": 
	app = web.application(urls, globals())
	app.run()  
