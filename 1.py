a=input("enter a string")
b=a[0]
i=1
print(a[0],end="")
while i<len(a):
    if b==a[i]:
        print("$",end="")
    else:
        print(a[i],end="")
    i=i+1
