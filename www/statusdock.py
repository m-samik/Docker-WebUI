#!/usr/bin/python3

print("content-type:text/html")
print()

import subprocess as sp
import cgi

cmd="sudo docker ps"

output=sp.getstatusoutput(cmd)
print("<center><img src = 'https://i.ibb.co/n7QJMJD/dc.png'></center>")
print("<center><h1>=======Status of Your Docker is Given Below =======</h1></center>")

print("<pre>")
print("<b>"+output+"</b>")
print("</pre>")

print("<center><a href='http://192.168.1.23/startd.html'>Go Back</a</center>")
