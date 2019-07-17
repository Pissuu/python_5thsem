f=open("colleges_list.txt",'r')
n=int(input("enter the number:"));
lines=f.readlines()
lines=lines[-n:]
for line in lines:
    print(line)
