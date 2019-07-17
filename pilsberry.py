a={'abc':123,'pqr':1234,'xyz':345}
l=list()
for i in a:
    l.append(i)
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[j]>l[i]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
for i in l:
    print(i)
