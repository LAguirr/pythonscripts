#!/usr/bin/env python
#_*_ coding: utf8 _*_


from shodan import Shodan
import sys



PYTHONIOENCODING="UTF-8"
key="41dtqbdZXkNrPnWNQoL03HZnU0vg24nr"

def main(): 
	api = Shodan(key)
	h = api.host('123.57.0.34')

	print('''

		Direccion: {}
		Ciudad: {}
		ISP: {}
		ORG: {}
		Puertos: {}


		'''.format(h['ip_str'], h['city'], h['isp'], h['org'], h['ports']))

	file = open('escane.txt', 'a+')

	for elemento in h['data']: 
		lista=elemento.keys()
		for l in lista: 
			file.write(str(elemento[l]))

	file.close()


if __name__ == '__main__':
	try: 
		main() 
	except: KeyboardInterrupt:
		exit()