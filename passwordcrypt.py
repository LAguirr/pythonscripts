#/usr/bin/env python
#_*_ coding: utf-8 _*_

import hashlib

def main(): 

	password = input("Palabra a cifrar: ").encode()

	md5pass = hashlib.md5(password).hexdigest()
	print("MD5: " + md5pass)

	sha1pass = hashlib.sha1(password).hexdigest()
	print("SHA1: " + sha1pass)

	sha224pass = hashlib.sha224(password).hexdigest()
	print("SHA224: " + sha224pass)

	sha256pass = hashlib.sha256(password).hexdigest()
	print("SHA256: " + sha256pass)

	sha384pass = hashlib.sha384(password).hexdigest()
	print("SHA384: " + sha384pass)

	sha512pass = hashlib.sha512(password).hexdigest()
	print("SHA512: " + sha512pass)



if __name__ == '__main__':
	main()