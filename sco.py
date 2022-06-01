#/usr/bin/env python
#_*_ coding: utf-8 _*_


import socket 

s = socket.socket()


try: 
	s.connect(("dlptest.com", 21))

	banner = s.recv(1024)
	print(banner)
except: 
	print("Ocurrio un error en la conexion")