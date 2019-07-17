str="yolallo"
d={}
for i in str:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)

