st="yo mama was so fat she gave enough blood for an entire blood bank"
words=st.split()
j=0
l=[]
for i in words:
    l.append((len(i),i))
l.sort(reverse=True)
for length,word in l:
    print(word,end=" ")
