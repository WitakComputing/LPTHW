formatter = "{} {} {} {}" #Curly brackets act like a formatter and when the function is called below, they are replaced with the string to be placed at the defined positon

print(formatter.format(1, 2, 3, 4)) #Double brackets are for lists inside a list
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "This is a money converter",
    "First attempt",
    "..",
    "...."
))
print ("USD to GBP money converter") #Mini money converter with Robins assist

formatter2 = "{Price:.2f} Pounds" #a variable which formats the value inputted to 2 decimal places

print(formatter2.format(Price=float(input("Please enter the amount in USD: "))/1.2322)) #prints the input and then multiplies the answer entered with
