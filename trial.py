import string
d={}
choice=1
def removepunc(file_name):
    count=0
    f=open(file_name)
    for line in f:
        line = line.translate(line.maketrans('','',string.punctuation))
        words=line.split()
        for w in words:
            d[w]=d.get(w,0)+1
            count=count+1
    print(count)
while(True):
    if choice==0:
        exit()
    file_name=input("enter the text document name: \t")
    removepunc(file_name)
    choice=input("if no more text documents to be considered please enter 0, else enter 1:\t")
    
