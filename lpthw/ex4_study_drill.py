cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
# if Error "NameError: name 'car_pool_capacity' is not defined" is found in line 8, its because the coder is suspected to be drunk/sleepy!! Line 7 defines a variable called "carpool_capacity" and not "car_pool_capacity"
#If space_in_a_car is assigned an int 4 then carpool_capacity would be an int and not a floating point number...
# = assignment operator -> assigns the valus on the right to the variable on the left. == comparision operatot
#Checking print w/o spaces...
print "Hey %s there." % "you"

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

