print("How old are you?", end='') #Question is printed with the end parameter which is used to add any string on the same line
age = input() #Variable which stores the age entered
print("How tall are you?", end='')
height = input()
print("How much do you weigh?", end='')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.") # prints the string alongside the data stored in the variables which would have been inputted by the user, uses f for format

print("What numbers would you like to multiply?", end='') #Does not work yet
Equation = input()

print ( f"The answer is {Equation}")