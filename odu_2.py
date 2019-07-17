import string
d={}
choice=1
def removepunc(file_name):
    count=0
    f=open(file_name)
    for line in f:
        line = line.translate(line.maketrans('','',string.punctuation))
        words=line.split()
        for i in words:
            count=count+1
        for w in words:
            d[w]=d.get(w,0)+1
    for i in d:
        d[i]=d[i]/count
    print(d)
    print(count)
while(choice==1):
    file_name=input("enter the text document name: \t")
    removepunc(file_name)
    choice=int(input("if no more text documents to be considered please enter 0, else enter 1:\t"))
    
