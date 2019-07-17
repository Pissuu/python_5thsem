import copy
def coor(point):
    """i can able to put it """
    print(point.x,point.y)
class point:
    """ can i able to do anything """
    x=0
    y=0
coor(point)
class rectangle:
    width=0
    height=0
    corner=point()
r=rectangle()
r.width=3
r.height=5
r.corner=point()
print("check")
print(r.width,r.height,r.corner)
r1=r
print("check")
print(r1 is r)
r2=copy.deepcopy(r)
print(r2 is r)
print(r2.corner is r.corner)
""" or put help(coor) """
    
