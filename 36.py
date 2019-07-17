import re
f=open("m3.txt","r")
for line in f:
    s=re.findall("^X\S*:\s[0-9]+[.]?[0-9]*$[\s\n]",line) 
    if s:
        print(s)
