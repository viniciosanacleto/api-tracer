import sys
import requests

args = sys.argv

if len(args)<3:
	sys.exit("Missing parameters: python3 crawl.py [API URL] [WORDLIST]")

url = args[1]
wlfile = args[2]

i = 0
with open(wlfile,'r') as file:
	readFile = file.read().splitlines()
	for word in readFile:
		r = requests.get(url+'/'+word)
		print(r.status_code)
