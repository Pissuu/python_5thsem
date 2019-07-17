class point:
    x=0
    y=0
    def __add__(self,others):
        p=point()
        p.x=self.x+others.x
        p.y=self.y+others.y
        return p
    def __str__(self):
        s=str(self.x)+","+str(self.y)
        return s

    def __init__(self,l=4,m=8):
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
print(p3)
d=point()
e=point()
print(d+e)
