#/usr/bin/env python
#_*_ coding: utf-8 _*_

from paramiko import client
from paramiko.ssh_exception import AuthenticationException
import threading
import time
import re


parser = argparse.ArgumentParser(description="Detector de tuneles")
parser.add_argument('-t','--target',help="Objetivo")
parser = parser.parse_args()

def brute(host, puerto, usuario, password): 
	log= paramiko.util.log_to_file('log.log')
	cliente = paramiko.SSHClient()
	cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	try: 
		cliente.connect(host, port=puerto, username=usuario, password = password)
		print("Credenciales {} : {} ".format(usuario, password))
	except: 
		print("Fallo la autenticacion")

def main(): 
		if parser.target: 

			ip = '10.81.120.4'
			puerto = 22
			usuario = 'leonel.hernandezaguirre@xpertal.com'
			password = 'Femsa*10'
			brute(ip, puerto, usuario, password)

if __name__ == '__main__':
	try: 
		main() 
	except KeyboardInterrupt: 
		exit() 
		