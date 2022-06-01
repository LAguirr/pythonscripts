#!/usr/bin/env python
#_*_ coding: utf8 _*_


from shodan import Shodan
import sys
import argparse


PYTHONIOENCODING="UTF-8"

parser = argparse.ArgumentParser()
parser.add_argument('-q','--query', help="busqueda")
parser.add_argument('-a','--api',help="Tu api")
parser = parser.parse_args()

def main():
	if parser.query: 
		
		if parser.api: 

			api = Shodan(parser.api)

			try: 
				b = api.search(parser.query)
				print("Print total de objetivos {}".format(b['total']))

				for i in b['matches']: 
					print("Target encontrado {}".format(i['ip_str']))


			except: 
				print("Error en la consulta")
		else: 
			print("Introduce tu api key")


	else: 
		print("Introduce un caracter de busqueda")



if __name__ == '__main__':
	try: 
		main() 
	except KeyboardInterrupt: 
		exit()