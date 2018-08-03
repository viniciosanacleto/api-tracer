import sys
import requests
import threading
from multiprocessing import Pool
from functools import partial

args = sys.argv

if len(args)<3:
	sys.exit("Use: python3 crawl.py [http://API_URL] [WORDLIST] [?THREADS]")

#ARGS
url = args[1]
wlfile = args[2]
if len(args)>3:
	nthreads = int(args[3])
else:
	nthreads = 50

#GLOBAL VARIABLES
wordlist = []

def doRequestGET(requestUrl):	
	r = requests.get(requestUrl)	
	if r.status_code == 200 or r.status_code == 401 or r.status_code == 400:
		print('GET: '+requestUrl)

def readFile():
	with open(wlfile,'r') as file:
		readFile = file.read().splitlines()
		for word in readFile:
			wordlist.append(url+'/'+word)


def main():
	readFile()
	if(len(wordlist)>0):
		print('This could take a while...\n')		
		#Do GET Requests
		with Pool(nthreads) as p:
			p.map(func,wordlist)	
	else:
		print('No words in wordlist!')

main()
