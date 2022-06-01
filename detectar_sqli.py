#!/usr/bin/env python
#_*_ coding: utf8 _*_

import mechanize
from bs4 import BeautifulSoup

nav = mechanize.Browser()
nav.set_handle_robots(False)
nav.set_handle_equiv(False)
nav.addheaders = [('User-Agent','Firefox')]
nav.open("https://curso-python-0-pruebas-pentest-dvwa.000webhostapp.com")
nav.select_form(nr=0)

nav['username'] = 'admin'
nav['password'] = 'password'

nav.submit()

nav.open("https://curso-python-0-pruebas-pentest-dvwa.000webhostapp.com/vulnerabilities/sqli/")
nav.select_form(nr=0)

nav['id'] = "'"

nav.submit()
soup = BeautifulSoup(nav.response().read(),'html5lib')
print(soup.pre.string)