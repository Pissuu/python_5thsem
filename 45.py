"""write an init method for the point class that takes x and y as optional
 parameters and assigns them to corresponding attributes, also define a
 method addpoints() to add two points and returns the added point object.
 print the added point object"""

class point:
    x=3
    y=4
    def __str__(self):
        s=str(self.x)#+","+str(self.y)
        return s
    def __init__(self,l=5,m=5):
        self.x=l
        self.y=m
    def addpoints(self,others):
        c=point()
        c.x=self.x+others.x
        c.y=self.y+others.y
        return c
        
p1=point(4,8)
p2=point()
p3=point()
p3=p1.addpoints(p2) # or point.addpoints(a,b)
print(p3)
            
#abhishek sent programme through mail
"""
class point:
    x=0
    y=0

    def __str__(self):
        s=str(self.x)+","+str(self.y)
        return s

    def __init__(self,l=0,m=0):
        self.x=l
        self.y=m
        
    def add_points(self,others):
        c = point()
        c.x=self.x+others.x
        c.y=self.y+others.y
        return c
a=point()
a.x=int(input("enter x cordinate"))
a.y=int(input("enter y cordinate"))
b=point()
b.x=int(input("enter x cordinate"))
b.y=int(input("enter y cordinate"))
p3=point()
p3=a.add_points(b)
print(p3) """
