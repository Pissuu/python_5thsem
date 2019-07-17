import math
class complex:
    real=0
    imaginary=0
    def multiply(self,others):
        val1=self.real*others.real
        val2=self.real*others.imaginary
        val3=self.imaginary*others.real
        val4=self.imaginary*others.imaginary
        print(val1,"+i*(",val2+val3,")+(-1)*(",val4,")")
s1=complex()
s2=complex()
s1.real=6
s1.imaginary=5
s2.real=5
s2.imaginary=2
s1.multiply(s2)
        
