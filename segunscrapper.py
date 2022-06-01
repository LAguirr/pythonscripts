#/usr/bin/env python
#_*_ coding: utf-8 _*_

def main(): 
	web = open('web.html', 'r')
	inicio = '<li>'
	final = '</li>'

	for l in web.readlines():

		if inicio in l: 

			
				ini = l.find(inicio)
				ini = ini + len(inicio)
				fin = l.find(final)

				print(l[ini:fin])


if __name__ == '__main__':
	main() 
