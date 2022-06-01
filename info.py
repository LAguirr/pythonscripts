#!/usr/bin/env python
#_*_ coding: utf8 _*_

from subprocess import check_output 
import subprocess

a = str(check_output('systeminfo',stderr = subprocess.STDOUT))

n = open('test.txt','w+')

n.write(a)
print("hola")

n.close()	