f=open("colleges_list.txt",'r')
n=int(input("enterthe number of lines to read"))
i=0
while i<n:
    txt=f.readline()
    print(txt)
    i=i+1
#for i in range(n):
#    line=f.readline()
#    print(line)
