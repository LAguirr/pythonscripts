#!/usr/bin/env python
#_*_ coding: utf8 _*_


from Wappalyzer import WebPages 


def main(): 
	wapp = Wappalyzer.latest() 

	try: 
		web = WebPage.new_from_url("https://zentius.proactivanet.com/proactivanet/")
		tecnologias = wapp.analyze(web)
		for t in tecnologias:
			print("Tecnologia detectada: {}".format(t))

	except:
		print("Ha ocurrido un error")


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo")
		exit()
