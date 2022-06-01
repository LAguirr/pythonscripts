#!/usr/bin/env python
#_*_ coding: utf8 _*_


from shodan import Shodan




PYTHONIOENCODING="UTF-8"
key="41dtqbdZXkNrPnWNQoL03HZnU0vg24nr"


motor = Shodan(key)
try:
	query = motor.search("struts")
	#total
	print("Total de resultados: {}".format(query['total']))
	#matches 

	for host in query['matches']:
		print("\nIP:  {}".format(host['ip_str']))
		print("puerto: {}".format(host['port']))
		print("ORG: {}".format(host['org']))

		try: 
			print("ASN {}".format(host['asn']))
		except: 
			pass

		for l in host['location']´:
			print(l + " : " + str(host['location'][l]))

		print(host['data'])

except: 
	Print("Ocurrio un error")
