a=[10,30,20,55,75,2]
j=0
k=0
for i in a:
    j=j+1
    k=k+i
print("no of elements:",j)
print("sum of elements",k)
k=0
j=0
k=a[0]
for i in a:
    if k>i:
        continue
    else:
        k=i
print("largest number is",k)
    
