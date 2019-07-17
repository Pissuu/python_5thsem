f=open("colleges_list.txt",'r')
lines=f.readlines()
for line in lines:
    if line.startswith("From:"):
        print(line)
