import re
s="hello232myword472program"
l=re.findall('([0-9][0-9]*)',s)
x=[]
for i in l:
    x.append(int(i))
print(max(x))

