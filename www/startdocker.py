#!/usr/bin/python3

print("content-type:text/html")
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()
name=form.getvalue("osname")
os=form.getvalue("ostype")

cmd="sudo docker run -dit --name {0} {1}".format(name,os)

output=sp.getstatusoutput(cmd)
status=output[0]
print("<center><img src = 'https://i.ibb.co/n7QJMJD/dc.png'></center>")
print("<center><h1>=======The Output of Your Docker O.S is given below =======</h1></center>")
if status==0:
    print("<h1>Your O.S with name: {} has been successfully Launched</h1>".format(name))
else:
    print("<h1>Your O.S has not been launched!! Check the Entered Value and try again Later</h1>")

print("<center><a href='http://192.168.1.23/startd.html'>Go Back</a</center>")
