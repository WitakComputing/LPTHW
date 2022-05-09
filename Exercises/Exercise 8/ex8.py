formatter = "{} {} {} {}" #Curly brackets act like a formatter and when the function is called below, they are replaced with the string to be placed at the defined positon

print(formatter.format(1, 2, 3, 4)) #Double brackets are for lists inside a list
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Konrad is awesome",
    "He's learning Python",
    "He will be a programmer",
    "He's the best"
))
