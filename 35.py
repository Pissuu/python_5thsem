import re
f=open("m3.txt")
for line in f:
    s=re.findall("^detail:\S*rev=([0-9]+)\.",line) 
    if s:
        for i in s:
            integer=int(i)
            if integer>0:
                print(integer)
