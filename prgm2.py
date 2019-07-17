s=input("enter string")
b=70-len(s)
def right_justified(s):
    i=0
    while i<=b:
        i=i+1
        print(' ',end='')
    print(s)
right_justified(s)
