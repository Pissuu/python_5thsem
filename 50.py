"""create an image file and download an image document
from the web browser"""

import urllib.request
f=urllib.request.urlopen("http://data.pr4e.org/cover3.jpg")
img=f.read()
f=open("image.jpg",'wb')
f.write(img)

