import string
d={}
s=input("enter a string")
s = s.translate(s.maketrans('','',string.punctuation))
word=s.split()
for w in word:
    d[w]=d.get(w,0)+1
print(d)
key=0
word=""
for word,count in d.items():
    if count>key:
        key=count
        w=word
print("the word with maximum frequency is:",key,w)
    
    
