import iLikePizza.web

class helloWorld(iLikePizza.web.Request):
	
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
	(r'^$', helloWorld),
	(r'^parm/([a-zA-Z_]*)$', helloWorld.parm),
	(r'remove$', helloWorld.remove),
	(r'set$', helloWorld.set),
])

if __name__ == "__main__":
	application.listen()