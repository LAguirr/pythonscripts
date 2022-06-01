#/usr/bin/env python
#_*_ coding: utf-8 _*_

import hashlib



def main(): 
	hashpass = str(input("HASH:  "))
	passfile = open("wordlist.lst",'r')
	for p in passfile.readlines(): 
		n = p.strip("\n").encode()
		n = hashlib.sha1(n).hexdigest()


		if n == hashpass: 
			print("Hola")
			print("Password: {}   HASH: {}".format(p, n))
			break

if __name__ == '__main__':
	main()