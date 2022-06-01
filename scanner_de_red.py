#/usr/bin/env python
#_*_ coding: utf-8 _*_


import nmap 


def main(): 
	nm = nmap.PortScanner()

	ip = input("IP: ")
	nm.scan(hosts=ip, arguments="--top-ports 1000 -sV --version-intensity 3")
	print("Comando ejecutado {}".format(nm.command_line()))
	#print(nm.scaninfo())
	print("Protocolos utilizados {}".format(nm[ip].all_protocols()))
	print("Estado de maquina:  {}".format(nm[ip].state()))
	print(nm[ip]['tcp'])
	for puerto in nm[ip]['tcp'].keys():
		for data in nm[ip]['tcp'][puerto]: 
			print(data + " : " + nm[ip]['tcp'][puerto][data])



if __name__ == '__main__':
	try: 
		main() 
	except KeyboardInterrupt:
		exit() 
