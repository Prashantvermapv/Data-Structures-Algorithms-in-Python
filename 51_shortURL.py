import hashlib

class UrlShortner:
	def __init__(self):
		self.short_to_url = dict()
		self.algo = hashlib.sha256

	def shorten(self, url):
		sha_signature = self.algo(url.encode()).hexdigest()
		# print(url.encode())
		print(sha_signature)
		short_hash = sha_signature[:6]
		print(short_hash)
		self.short_to_url[short_hash] = url
		return short_hash

	def restore(self, short_hash):
		return self.short_to_url[short_hash]

url = "https://teams.microsoft.com/_#/calendarv2"
US = UrlShortner()
short = US.shorten(url)
assert US.restore(short) == url
