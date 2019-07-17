"""define a function increment() which takes time object and a number(in seconds)
with which the time object has to be increased .Define a function mul_time()
that takes a time object and a number and returns a new time object that
contains the product of the original time and the number.
then use the function mul_time() to define a function that takes time object
that represents the finishing time in a race, and a number that represents the
distance, and returns the time object that represents the average pace(times
per mile) """

def increment(t,number):
    n1=time_to_int(t)+number
    return int_to_time(n1)

def mul_time(t,num):
    result=time_to_int(t)*num
    return int_to_time(result)

def time_to_int(t):
    return (t.hours*3600+t.mins*60+t.secs)

def int_to_time(t):
    t=Time()
    t.mins,t.secs=divmod(seconds,60)
    t.hours,t.mins=divmod(t.mins,60)
    printime(t)
    
def printime(t):
    print(t.hours,":",t.mins,":",t.secs)

end=Time()
end.hours=2
end.mins=30
end.secs=40
distance=13
oace=mul_time(end,1/distance)


class Time:
    t=Time()
    t.hours=1
    t.mins=30
    t.sec=55
    t1=Time()
##refer notes and use the functions defined
    
    
