def sed(pat,rep,f1,f2):
    f1=open(f1,'r')
    f2=open(f2,'w')   
    p=f1.read()
    for i in p:
        p=p.replace(pat,rep)
    f2.write(p)
pat=input("enter a pattern")
rep=input("enter string")
f1=input("enter file name")
f2=input("enter file name:")
sed(pat,rep,f1,f2)
    
