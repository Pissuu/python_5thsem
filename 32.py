f=open("file1.txt")
d={}
l=[]
for lines in f:
    words=lines.split()
    for word in words:
        if word not in d:
            d[word]=1
        else:
            d[word]+=1
for word,count in d.items():
    l.append((count,word))
l.sort(reverse=True)
for count,word in l[ :10]:
    print(count,word,end=" ") 
