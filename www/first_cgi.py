#! /usr/bin/python3
print("content-type:text/html")
print()

import subprocess
output=subprocess.getoutput("date")
print(output)
print("\n")
x="Programe Running Good...\n"

print(x)
