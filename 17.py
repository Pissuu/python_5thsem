i=0
l1=list()
sum=0
while(1):
    a=input("enter a number")
    i=i+1
    if(a=="done"):
        i=i-1
        break
    l1.append(int(a))
    sum=sum+int(a)
print("count is ",i ,"and sum is",sum)
