import string
choice=1
first=1
listv=[]
listk=[]
fn=[]
strings=""
number1list=[]
def norm(dicty):
    for value,key in dicty.items():
        for i in listv[ : ]:    
            if i==value:                                     #matches words in the forst doc with words from remaining docs
                ind=listv.index(i)                           #if match condition occurs lists are updated i.e. the total number of occurances are updated in listk
                listk[ind]=listk[ind]+key
def removepunc(file_name):
    cnt=0                                                    #initialising variables
    count=0
    l=string.punctuation
    f=open(file_name)
    for line in f:
        for i in l:
            line=line.replace(i," ")
        words=line.split()
        for i in words:
            count=count+1
        for w in words:
            dicty[w]=(dicty.get(w,0)+1)
    print("the occurance of each word in the document:",file_name,"is")
    for i in dicty.items():
        print(i)
    for i in dicty:
        dicty[i]=dicty[i]/count
    if first==1:
        for value,key in dicty.items():
            listv.append(value)
            listk.append(key)
        for value,key in dicty.items():
            number1list.append((value,key)) 
    if(first!=1):
        norm(dicty)
    print("the frequency of words in the text file:",file_name,"is")
    for i in dicty.items():
        print(i)
while(choice==1):                                            #input is accepted as long as choice remains 1
    file_name=input("enter the text document name: \t")      #accepts file name as input
    fn.append(file_name)                                     #filenames are inserted into a list for reference later
    l=string.punctuation
    f=open(file_name)
    for line in f:
        for i in l:
            line=line.replace(i," ")
        strings=strings+line    """ all lines are added to a string """
    dicty=file_name+"dictionary"                             #unique dictionary ids are created
    dicty={}                                                 #dictionaries are defined
    removepunc(file_name)                                    #function is called
    first=2                                                  #variable first is incremented 
    choice=int(input("if no more text documents to be considered please enter 0, else enter 1:\t")) #users input is accepted
dictionary={}                                                #dictionary is defined
words=strings.split()
for w in words:
    dictionary[w]=(dictionary.get(w,0)+1)
print("The required unique characters across the documents are: \n")   
for val,key in dictionary.items():
    print(val,end=" ")
number=0
l=string.punctuation                                         #has a list of punctuation marks 
for i in fn[ : ]:
    ind=0
    number=number+1
    print("\n")
    print("In the",number,"document\t")
    di={}
    cnt=0
    f=open(i)
    for line in f:
        for i in l:
            line=line.replace(i," ")                         #replaces all punctuations with white spaces
        words=line.split()
        for i in words:
            cnt=cnt+1
        for w in words:
            di[w]=(di.get(w,0)+1)
    for i in di:
        di[i]=di[i]/cnt
    for value,key in di.items():
        for i in listv[ : ]:
            if value==i:
                ind=listv.index(i)  
                div=key/listk[ind]                          #does the division
                print(value,"has a normal doc score of",key,"/",listk[ind],"=",div) 



    
