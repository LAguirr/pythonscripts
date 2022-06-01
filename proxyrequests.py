import requests


def main(): 
	a = requests.get("https://ifconfig.me")
	print("IP sin proxys:  {}".format(a.text))

	proxy = {
		'http':'http://8.9.3.70:8080',	
		'https': 'http://8.9.3.70:8080'
	}

	b = requests.get('https://ifconfig.me', proxies=proxy)

	print('IP con proxys: {}'.format(b.text))




if __name__ == '__main__':
	main()