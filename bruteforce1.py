#/usr/bin/env python
#_*_ coding: utf-8 _*_


import hashlib

from urllib import request


def main(): 
	hashpass = input("HASH:  ")
	passwordlist = request.urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt").read()
	
	for p in passwordlist.split('\n'):
		z = hashlib.md5(p).hexdigest()
		if z == hashpass: 
			print("Password: {}    HASH:  {}".format(p, z))



if __name__ == '__main__':
	try: 
		main()
	except KeyboardInterrupt: 
		print("Saliendo")
		exit()