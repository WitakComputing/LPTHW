cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

#Study drill error: The variable has a spelling mistake therefore its not found

#Study drill 1&2: Decimal is not necessary, it will work with as an integer(Full number)

#Study drill 3: Comments are written above
#Study drill 4: = is equals and its purpose is to give data names.
#Study drill 5: _ is an underscore and its used to add space in words alongside other things
#Study drill 6: done  