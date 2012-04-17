import iLikePizza.web
import iLikePizza.debugger 

class helloWorld(iLikePizza.web.Request):
	
	def initialize(self):
		print "init helloWorld"
		
	def get(self):
		return "index"
	
	def post(self):
		return "post"
		
	def custom(self):
		return "hi there"

application = iLikePizza.web.Application([
	(r'^$', helloWorld),
	(r'test/([a-zA-Z_]*)$', helloWorld.custom),
])

if __name__ == "__main__":
	application.listen()