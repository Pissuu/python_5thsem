f=open('words.txt','r')
d=dict()
j=0
for line in f:
    words=line.split()
    for i in words:
        if i not in d:
            d[i]=j
            j+=1
print(d)
search=input("enter a string")
if search in d:
    print("string found")
else:
    print("string not found")
