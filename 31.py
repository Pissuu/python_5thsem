d={'a':50,'b':20,'c':40}
l=[]
for key,val in d.items():
    l.append((val,key))
l.sort(reverse=True)
for val,key in l:
   print(key,val,end=" ")

