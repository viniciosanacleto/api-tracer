import sys
import requests
import threading
import math
from multiprocessing import Pool

args = sys.argv

if len(args)<3:
	sys.exit("Use: python3 crawl.py [http://API_URL] [WORDLIST]")

url = args[1]
wlfile = args[2]
wordlist = []
nthreads = 50

def doRequest(requestUrl):
	r = requests.get(requestUrl)	
	if r.status_code == 200 or r.status_code == 401:
		print('Gotcha: '+requestUrl)

def readFile():
	with open(wlfile,'r') as file:
		readFile = file.read().splitlines()
		for word in readFile:
			wordlist.append(url+'/'+word)


def main():
	readFile()
	if(len(wordlist)>0):
		print('This could take a while...')
		with Pool(nthreads) as p:
			p.map(doRequest,wordlist)	
	else:
		print('No words in wordlist!')

main()
