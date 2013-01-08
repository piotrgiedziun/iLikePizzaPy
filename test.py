import iLikePizza.web

class staticFilesHandler(iLikePizza.web.Static):
	folder = "public"

class helloWorldHandler(iLikePizza.web.Request):
	
	#def initialize(self):
	#	# db connection here
	#	print "init helloWorld"
		
	def get(self):
		# show cookie and session values
		cookie = self.get_cookie("index", "none")
		session = self.get_session("test", "none")

		self.write("GET METHOD\nCOOKIE VALUE=%s\nSESSION VALUE=%s" % (cookie,session) )
		
	def post(self):
		# render template
		self.render("test.html", test=1, test2=2)
		
	def remove(self):
		# remove data
		self.remove_cookie("index")
		self.remove_session()
		# write output
		self.write("remove action done!")
		
	def set(self):
		# set data
		self.set_cookie("index", "value")
		self.set_session("test", "test value")
		# write output
		self.write("set action done!")
		
	def parm(self, parm=None):
		self.write("%w" % (parm,) )

application = iLikePizza.web.Application([
	(r'^$', helloWorldHandler),
	(r'^parm/([a-zA-Z_]*)$', helloWorldHandler.parm),
	(r'remove$', helloWorldHandler.remove),
	(r'set$', helloWorldHandler.set),
	(r'public/([a-zA-Z_.]*)$', staticFilesHandler.handle),
])

if __name__ == "__main__":
	application.listen()