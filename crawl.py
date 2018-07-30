import sys
import urllib3

args = sys.argv
http = urllib3.PoolManager()

if len(args)<3:
	sys.exit("Missing parameters: python3 crawl.py [API URL] [WORDLIST]")

url = args[1]
wlfile = args[2]

i = 0
with open(wlfile,'r') as file:
	for word in file:
		requestUrl = url+'/'+word
#		print(requestUrl)
		r = http.request('GET',requestUrl)
#		print(r.status_code)
		print(r.status)
