import web

render = web.template.render('setdirectory/')
urls = (
	'/', 'boom'
)

class boom:
	def GET(self):
		i = web.input(name=None)
		return render.setweb(i.name,'test')

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()