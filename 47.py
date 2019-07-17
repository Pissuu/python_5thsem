import math
class complex:
    real1=0
    imaginary=0
    def __lt__(self,others):
        if(self.real1<others.real1):
            return True
        else:
            return False
            

    def __str__(self):
        s=str(self.real1)+","+str(self.imaginary)
        return s

    def __init__(self,l=4,m=8):
        self.real1=l
        self.imaginary=m             
        

    def com_mul(self,others):
        value1=complex()
        value1.real1 = self.real1*others.real1+self.imaginary*others.imaginary*-1
        value1.imaginary = self.real1*others.real1+self.imaginary*others.imaginary
        return value1

c=complex()
d=complex(5)

e=complex()
e=complex.com_mul(c,d)
print(c<d)
