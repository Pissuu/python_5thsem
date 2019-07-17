import re
f=open("m3.txt")
for line in f:
    s=re.findall("[a-zA-Z0-9]\S*@[a-zA-Z]+\.[a-zA-Z]+",line)
    if s:
        for i in s:
            print(i)
    
