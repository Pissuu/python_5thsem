f=open("colleges_list.txt")
lines=f.readlines()
for line in lines:
    #if(line.find("from",0,5)==0):
    if line.startswith("from"):
        print(line)
