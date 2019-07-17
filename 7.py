a=int(input("enter the width"))
b=input("enter the number")
c=len(b)

if a>c:
    c=a-len(b)
    i=0
    while i<c:
        print("0",end="")
        i=i+1
print(b)
