#/usr/bin/env python
#_*_ coding: utf-8 _*_

import mechanize

from bs4 import BeautifulSoup

nav = mechanize.Browser()
nav.set_handle_robots(False)
nav.set_handle_equiv(False)
nav.addheaders=[('User-Agent','Firefox')]
nav.open("https://curso-python-0-pruebas-pentest-dvwa1.000webhostapp.com/login.php")

#for f in nav.forms(): 
#	print(f)
nav.select_form(nr=0)

nav['username'] = 'admin'
nav['password'] = 'password'

nav.submit()

print(nav.response().read())

nav.open("https://curso-python-0-pruebas-pentest-dvwa1.000webhostapp.com/vulnerabilities/sqli/")
#for f  in nav.forms(): 
#	print (f)

nav.select_form(nr=0)

nav['id'] = "'"  #'1'

nav.submit()
print(nav.response().read())

soup = BeautifulSoup(nav.response().read(), 'html5lib')

print(soup.pre.string)
