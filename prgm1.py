import math
number=int(input("enter number"))     
def cube(number):
    b=number**3
    print(b)
def by_three(number):
    if number%3==0:
        cube(number)
    else :
        print("false")
by_three(number)
cube(number)
    
