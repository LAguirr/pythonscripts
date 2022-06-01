#!/usr/bin/env python
#_*_ coding: utf8 _*_ 


import requests 
from bs4 import BeautifulSoup 

def main(): 
	url =  "https://es.wordpress.com/"
	cabecera= {'User-Agent':'Firefox	'}
	peticion = requests.get(url=url,headers=cabecera) 
	

	soup = BeautifulSoup(peticion.text, 'html5lib')

	for v in soup.find_all('meta'):
		if v.get("name") == "generator": 
			version = v.get("content")
	print(version) 


if __name__ == '__main__':
	try: 
		main()

	except KeyboardInterrupt: 
		print("Saliendo")
		exit()
