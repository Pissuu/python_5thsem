def removepunk(word):
    s=word
    b=""
    for i in range(0,len(s)):
        a=ord(s[i])
        if (a>=65 and a<=90) or (a>=97 and a<=122):
            b=b+s[i]
    return b
f=open('m1.txt','r')
d={}
i=1
for line in f:
    words=line.split()
    for word in words:
        word=removepunk(word)
        if word not in d:
            d[word]=1
        else:
            d[word]=d[word]+1
            
print(d)

