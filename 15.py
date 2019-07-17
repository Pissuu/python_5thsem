f=open("colleges_list.txt",'r')
lines=f.readlines()
for line in lines:
    if line.find("From:")!=-1:
        print(line)
