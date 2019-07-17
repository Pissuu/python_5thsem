class rectangle:
    """ can i able to do anything """
    width=0
    height=0
r=rectangle()
def findcentre():
    xcorner=int(input("enter the corner x cordinated"))
    ycorner=int(input("enter thye corner y cordinates"))
    r.width=int(input("enter the width"))
    r.height=int(input("enter the height"))
    xcentre=0
    ycentre=0
    xcentre=xcorner+r.width/2
    ycentre=ycorner+r.height/2
    print(xcentre,ycentre)
findcentre()
    
