#!/home2/silviolo/python/bin/python 
# -*- coding: utf-8 -*-

# MODULES

import web
from getImgUrl import randWord, search
from getImgUrlDb import searchDb

render = web.template.render('templates/')

urls = (
  '/', 'index'
)

class index:
	def GET(self):
		term = searchDb()
    # direct query to Google:
    # term = search(randWord())
		return render.index(term[0], term[1])

web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
if __name__ == "__main__": 
	app = web.application(urls, globals())
	app.run()  
