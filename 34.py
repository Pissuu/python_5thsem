import re
f=open("m3.txt")
for line in f:
    s=re.findall("X\S*:\s([0-9]+)",line) #prints only the number part of the expression
    if s:
        print(s)
