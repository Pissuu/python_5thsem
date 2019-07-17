f=open('mailog.txt')
d={}
for line in f:
    b=line.startswith("From")
    if b!=-1:
        words=line.split()
        for word in words:
            if word.find('@')!=-1:
                if word not in d:
                    d[word]=1
                else:
                    d[word]=d[word]+1
print(d)

