nights=int(input("enter the number of nights"))
city=input("enter the city")
def plane_ride(city):
    if city=="bengaluru":
        args=5000
        print(args)
        hotel_cost(nights)
    elif city=="hyderabad":
        args=4500
        print(args)
        hotel_cost(nights)
    else:
       print("error")
def hotel_cost(nights):
    cost=1400*nights
    print("cost of stay is:",cost)
    trip_cost(args,cost)
def trip_cost(args,cost):
    cost1=args+cost
    print("total",cost1)
plane_ride(city)
