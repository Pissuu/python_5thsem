lst=[2,3,4,5]
length=len(lst)
def is_sorted(l,cnt):
    i=0
    l2=list(l)
    l.sort()
    print(l)
    print(l2)
    while i<length:
        if l2[i]!=l[i]:
            print("not in order")
            break
        else:
            cnt=cnt+1
        i=i+1
    return cnt
cnt=is_sorted(lst,0)            
if cnt==length:
    print("in order")

