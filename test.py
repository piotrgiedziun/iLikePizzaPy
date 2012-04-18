import iLikePizza.web

class helloWorld(iLikePizza.web.Request):
	
	def initialize(self):
		print "init helloWorld"
		
	def get(self):
		self.write("GET METHOD\nCOOKIE VALUE=%s" % (self.get_cookie("index", "not set"),) )
	
	def post(self):
		self.render("test.html", test=1, test2=2)
		
	def custom(self, parm=None):
		self.set_cookie("index", "value")
		
		self.write("set cookie")

application = iLikePizza.web.Application([
	(r'^$', helloWorld),
	(r'test/([a-zA-Z_]*)$', helloWorld.custom),
])

if __name__ == "__main__":
	application.listen()