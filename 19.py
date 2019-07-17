l=[10,20,30,30,20,5]
for i in l:
    print(i)
print("length of the list is",len(l))
i=0
j=0
while i<len(l):
    j=i+1
    while j<len(l):
        if l[i]==l[j]:
            x=l.pop(j)
        else:
            j=j+1
    i=i+1
print("after removing redundancy")
for i in l:
    print(i)
