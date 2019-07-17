""" define a function valid_time() that takes a time object that returns true
if the time is valid else it returns false"""

class Time():
    hours=0
    mins=0
    secs=0
t=Time()
t.hours=2
t.mins=7
t.secs=20

def valid_time(t):
    if t.hours<0 or t.mins<0 or t.secs<0 or t.mins>=60 or t.secs>=60:
        return False
    return True

def exception(t):
    assert valid_time(t),"true is dgood food"
    if True is valid_time(t):
        print("valid time")

exception(t)
