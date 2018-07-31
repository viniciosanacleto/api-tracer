import sys
import requests
import threading
import math

args = sys.argv

if len(args)<3:
	sys.exit("Use: python3 crawl.py [http://API_URL] [WORDLIST]")

url = args[1]
wlfile = args[2]
wordlist = []
chunks = []
nthreads = 3

def doRequest(requestUrl):
	r = requests.get(requestUrl)
	if r.status_code == 200 or r.status_code == 401:
		print('Gotcha: '+requestUrl)

def readFile():
	with open(wlfile,'r') as file:
		readFile = file.read().splitlines()
		for word in readFile:
			wordlist.append(word)

def splitWordList():
	chunk_size = len(wordlist) / nthreads
	l = []
	i = 1
	for word in wordlist:
		l.append(word)
		i += 1
		if i == chunk_size:
			chunks.append(l)
			l = []
			i = 0
		
def main():
	i = 0
	readFile()
	splitWordList()
	print(chunks)
	if(len(wordlist)>0):
		for word in wordlist:
			doRequest(url+'/'+word)
			i += 1
			if i%1000 == 0:
				print(i)
	else:
		print('No words in wordlist!')

main()
