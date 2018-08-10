import sys
import requests
import threading
from multiprocessing import Pool
from functools import partial
from args import solveArgs

##################
#GLOBAL VARIABLES
##################
wordlist = []
##################
#ARGS
##################
args = sys.argv
if len(args)<3:
	print("Use: python3 crawl.py [http://API_URL] [WORDLIST] [?OPTIONS]")
	sys.exit()

url = args[1]
wlfile = args[2]

args = solveArgs(args)

def configByArgs():
	if('threads' not in args):
		args['threads'] = 50

def doRequestGET(requestUrl):	
	r = requests.get(requestUrl)	
	if r.status_code == 200 or r.status_code == 401 or r.status_code == 400:
		print('GET: '+requestUrl)

def doRequestPOST(requestUrl):	
	r = requests.post(requestUrl)	
	if r.status_code == 200 or r.status_code == 401 or r.status_code == 400:
		print('POST: '+requestUrl)

def doRequestPUT(requestUrl):	
	r = requests.put(requestUrl)	
	if r.status_code == 200 or r.status_code == 401 or r.status_code == 400:
		print('PUT: '+requestUrl)

def doRequestDELETE(requestUrl):	
	r = requests.delete(requestUrl)	
	if r.status_code == 200 or r.status_code == 401 or r.status_code == 400:
		print('DELETE: '+requestUrl)

def readFile():
	with open(wlfile,'r') as file:
		readFile = file.read().splitlines()
		for word in readFile:
			wordlist.append(url+'/'+word)


def main():
	configByArgs()
	readFile()
	if(len(wordlist)>0):
		print('This could take a while...\n')		
		#Do GET Requests
		with Pool(args['threads']) as p:
			p.map(doRequestGET,wordlist)
			p.map(doRequestPOST,wordlist)
			p.map(doRequestPUT,wordlist)
			p.map(doRequestDELETE,wordlist)

	else:
		print('No words in wordlist!')

main()
