#/usr/bin/env python
#_*_ coding: utf-8 _*_


import requests
import argparse


parser = argparse.ArgumentParser(description="Detector de cabecera")
parser.add_argument('-t', '--target', help="Objetivo")
parser = parser.parse_args()

def  main():
	if parser.target: 
		try: 
			url = requests.get(url=parser.target)
			cabecera = dict(url.headers)
			for x in cabecera: 
				print(x + ' : ' + cabecera[x])

		except: 
			print("No se pudo conectar ")

	else: 
		print("No hay objetivo")



if __name__ == '__main__':
	main() 