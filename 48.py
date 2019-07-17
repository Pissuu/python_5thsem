import urllib.request
f=urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in f:
    print(line.decode())
