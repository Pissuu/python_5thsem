""" write a definition for a class named circle with attributes centre and
radius, where centre is a point obj. and radius is a no. . instantiate a circle
obj. that represents a circle with its centre at 150,100 and radius 75.
Write a function named point_in_circle() that takes a circle and a point
a returns true if the point lies within or on the boundary of the circle.
Write a function named rect_in_circle() that takes a circle and a rectangle and
returns true if the rectangle lies entirely in or on the boundary of the circle"""
choice=0
class point:
    x=0
    y=0
class circle:
    r=0
    centre=0
centre=point()
c1=circle()
centre.x=150
centre.y=100
c1.r=75
def point_in_circle(a,b,rad):
    c=int(input("enter the x coordinate of the point:\t"))
    d=int(input("enter the y coordinate of the point:\t"))
    adown=a-rad
    """ use math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))<=75 then in or on the circle """
    #math.pow for calculating powers
    aup=a+rad
    bdown=b-rad
    bup=b+rad
    if c>=adown and c<=aup and d>=bdown and d<=bup:
         print("True")
    else:
        print("False")
def point_in_circle_rect(c,d,a,b,rad):
    adown=a-rad
    aup=a+rad
    bdown=b-rad
    bup=b+rad
    if c>=adown and c<=aup and d>=bdown and d<=bup:
         print("True")
    else:
        print("False")
def rect_in_circle(a,b,rad):
    c=int(input("enter the x coordinate of the corner of the rectangle:\t"))
    d=int(input("enter the y coordinate of the rectangle:\t"))
    width=int(input("enter the width of the rectangle:\t"))
    height=int(input("enter the height of the rectangle:\t"))
    #corner one is c,d
    point_in_circle_rect(c,d,centre.x,centre.y,c1.r)
    c2=c
    c3=c+height
    point_in_circle_rect(c2,c3,centre.x,centre.y,c1.r)
    c4=c+width
    c5=c+height
    point_in_circle_rect(c4,c5,centre.x,centre.y,c1.r)
    c6=c+width
    c7=c
    point_in_circle_rect(c6,c7,centre.x,centre.y,c1.r)
    print("if true is printed 4 times then the rectangle is within the circle else its not")
    adown=a-rad
    aup=a+rad
    bdown=b-rad
    bup=b+rad
    if c>=adown and c<=aup and d>=bdown and d<=bup:
         print("True")
    else:
        print("False")
while choice!=1:
    point_in_circle(centre.x,centre.y,c1.r)
    rect_in_circle(centre.x,centre.y,c1.r)
    choice=int(input("enter 1 to exit and 0 to continue"))
    if choice==1:
        exit()
