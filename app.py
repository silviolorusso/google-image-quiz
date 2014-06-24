#!/home2/silviolo/python/bin/python 
# -*- coding: utf-8 -*-

# MODULES

import web
from getImgUrl import search
from getImgUrlDb import searchDb

render = web.template.render('templates/')

urls = (
  '/', 'index'
)

class index:
	def GET(self):
		term = search()
		# be sure google doesn't complain
		try:
			print term[0]
			print term[1]
		# else pick term from db
		except:
		 	term = searchDb()
		return render.index(term[0], term[1])

web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
if __name__ == "__main__": 
	app = web.application(urls, globals())
	app.run()  
