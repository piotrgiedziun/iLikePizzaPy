import Cookie
import uuid
import time

class CookiesManager(object):
	
	def __init__(self, http_cookie):
		self._cookie = Cookie.SimpleCookie(http_cookie)
	
	def set(self, index, value, expires_time=30*24*60*60):
		self._cookie[index] = value
		self._cookie[index]["path"] = "/"
		self._cookie[index]["expires"] = expires_time
		self._cookie[index]["version"] = 1
		
	def get(self, index, default=None):
		print self._cookie[index]
		try:
			return self._cookie[index].value
		except:
			return default
			
	def remove(self, index):
		pass
		
	def remove_all(self):
		pass
	
	def get_headers(self):
		return [
			("Set-Cookie", self._cookie.output(header="Set-Cookie:")[len("Set-Cookie:"):]),
			("Cookie", self._cookie.output(header="Cookie:")[len("Cookie:"):]),
		]
			
			
class SessionManager(CookiesManager):
		
	def session_start(self):
		# create session
		super(SessionManager, self).set("session", uuid.uuid1())
