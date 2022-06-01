#/usr/bin/env python
#_*_ coding: utf-8 _*_
 import re 
 import urllib

 def get_li:

 	code = urllib.urlopen('https://lorem2.com/')
 	code = code.read()
 	todo = re.findall('<li>(.+)</li>', code)
 	for t in todo: 
 		if not "<a href=" in t: 
 			print(t + '\n')


 def main():
 	get_li()



 if __name__ == '__main__':
 	main()
