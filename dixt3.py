import string
d={}
f=open('txt1.txt')
for line in f:
    line = line.translate(line.maketrans('','',string.punctuation))
    words=line.split()
    for w in words:
        d[w]=d.get(w,0)+1
print(d)
