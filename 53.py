"""write a programto retireve the data from "romeo.txt" and compute the frequency of each
word in the file . note that the file is stored on the server and not on the local
comp that u r coding on."""

import urllib.request
fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
