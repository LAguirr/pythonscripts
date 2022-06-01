import socks
import requests
import socket
import json


def main(): 
	print('Peticion sin TOR:  ' + requests.get('https://ifconfig.me').text)

	socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9050)

	socket.socket = socks.socksocket

	p = requests.get('https://ifconfig.me')
	data1 = requests.get('https://ipinfo.io/{}'.format(p.text))

	data = json.loads(data1.text)	

	print('Peticion con TOR: ' + p.text + '\tCiudad: {}'.format(data['city']))

if __name__ == '__main__':
	main()