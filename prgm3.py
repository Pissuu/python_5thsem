arg=-5
def distance_from_zero(arg):
    if type(arg)==int:
        print(abs(arg))
    elif type(arg)==str:
        print("nope")
    else:
        print("pope")
distance_from_zero(arg)
