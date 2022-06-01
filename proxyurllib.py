import urllib.request


def main(): 
	

#Peticion sin proxy
	p = urllib.request.urlopen('https://ifconfig.me')
	print("IP sin proxy: {}".format(p.read()))

	#configuramos el proxy

	urllib.request.install_opener(
		urllib.request.build_opener(
			urllib.request.ProxyHandler(
				{
					'http':'http://8.9.3.70:8080',	
					'https': 'http://8.9.3.70:8080'
				}
			)
		)
	)

	peticion = urllib.request.urlopen('https://ifconfig.me')

	print('IP con Proxy: {}'.format(peticion.read()))


if __name__ == '__main__':
	main()