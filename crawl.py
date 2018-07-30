import sys
import requests

args = sys.argv

if len(args)<3:
	sys.exit("Use: python3 crawl.py [http://API_URL] [WORDLIST]")

url = args[1]
wlfile = args[2]

i = 0
with open(wlfile,'r') as file:
	readFile = file.read().splitlines()
	print('This could take a while...')
	for word in readFile:
		i += 1
		requestUrl = url+'/'+word
		r = requests.get(requestUrl)
		if r.status_code == 200 or r.status_code == 401:
			print('Gotcha: '+requestUrl)
		if i%1000 == 0:
			print(i)
