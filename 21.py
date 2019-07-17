t=[[1,2],[3],[4,5,6],6]
e=list()
sum1=0
for i in t:
    if type(i)==list:
        sum1=sum1+sum(i)
    else:
        sum1=sum1+i
print(sum1)
