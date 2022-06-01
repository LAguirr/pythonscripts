#!/usr/bin/env python
#_*_ coding: utf8 _*_

import requests 
import argparse
from os import path


parser = argparse.ArgumentParser()
parser.add_argument('-f','--file',help="Indica el archivo a subir")
parser = parser.parse_args()

def main(): 
	if parser.file: 
		if path.exists(parser.file): 
			archivo = open(parser.file,'rb')
			headers = {'User-Agent':'Firefox'}
			peticion = requests.post(url="https://curso--python-0-prueba-pentest.000webhostapp.com/index.php",files={'uploaded_file':archivo},headers=headers )
			if parser.file in peticion.text: 
				print(peticion.text)
				print("Archivo subido con exito")
			else: 
				print("Fallo la subida del archivo")
		else: 
			print("No existe el archivo")
	else: 
		print("Necesito un archivo para subir")

if __name__ == '__main__':
	try: 
		main()
	except KeyboardInterrupt: 
		print("Saliendo...")