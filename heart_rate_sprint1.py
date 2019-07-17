heart_list=[]
i=0
l=","
f=open("fit_bit.csv","r")
f1 = open("fit_bit.txt","w")
for line in f:
    line=line.replace(l," ")
    print(line)
    f1.write(line)
j=0
row_no=-1
word_no=-1
f1 = open("fit_bit.txt","r")
f2 = open("fit_bit_exctract.txt","w")
for line in f1:
    j=j+1
    k=0
    words=line.split()
    for i in words:
        k=k+1
        if i=="BMI":
            word_no=k;
            row_no=j;
            ##print(j) j has line number in which BMI exists
            ##print(word_number) word_number has the column position of required data
        if j>row_no and k==word_no:
            ##i.remove
            f2.write(i)
f2.close()
f.close()
f1.close()
        



