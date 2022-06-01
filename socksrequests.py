import requests

def main(): 
	a = requests.get('https://ifconfig.me')
	print('Peticion sin SOCKS:  {}'.format(a.text))

	proxy = {
		'http':'http://96.44.183.149:55225',
		'https':'https://96.44.183.149:55225'
	}

	b = requests.get('https://ifconfig.me',proxies=proxy)
	print("IP con SOCKS: {}".format(b.text))



if __name__ == '__main__':
	main()