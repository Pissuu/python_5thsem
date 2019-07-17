a=input("enter a string")##refer notes for easier code
i=0
if len(a)<3:
    print(a)
else:
    i=len(a)-4
    if(a[i]=="i"):
        if(a[i+1]=="n"):
            if(a[i+2]=="g"):
                i=0
                while i<len(a)-4:
                    b[i]=a[i]
                    i=i+1
                b[i+3]="l"
                b[i+1]="y"
    else:
        i=0
        while i<len(a)-4:
            b[i]=a[i]
            i=i+1
        b[i+1]="i"
        b[i+2]="n"
        b[i+3]="g"
            
            
