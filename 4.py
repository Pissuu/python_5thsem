def first(s):    
    b=s.find("not")
    c=s.find("poor")
    if c>b and b>=0:
     s1=s[0:b]+"good" +s[c+4: ]
     return s1
    else:
        return s
print(first("ram is not that poor"))    

