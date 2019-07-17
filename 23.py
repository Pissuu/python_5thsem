def funct():
    l1=[10,20,30,40]
    l2=[40,50,60]
    for i in l1:
        for j in l2:
            if i==j:
                print("has common member")
                return
    print("no common members")
funct()
