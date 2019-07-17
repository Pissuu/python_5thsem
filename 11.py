data="jaba mxyz"
i=0
for i in range(len(data)):
    b=ord(data[i])
    if b>122:
        print("-",end="")
    if b<97:
        print("-",end="")
    if 97<b<123:
        if 114<b<123:
            b=b-26                        #small error somewhere
    b=b+7
    print(chr(b),end="")
    
        
