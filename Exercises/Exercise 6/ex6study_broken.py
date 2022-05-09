# Study drill to break the code
types_of_people = 10 # This is a variable which stores the number of people
x = f"There are {types_of_people} types of people." # A variable which stores an f-string 

binary = "binary" # A variable storing a string
do_not = "don't" # A variable storing a string
y = f"Those who know {binary} and those who {do_not}." # A variable storing an f-string (a string with variables embedded)

print(x) # Prints variable x
print(y) # Prints variable y

print(f"I said: {x}") # Prints f-string that contains a variable
print(f"I also said: {y}") # Prints f-string that contails a variable 

hilarious = True # A boolean variable. Boolean can only hold two values, true or false.
joke_evaluation = "Isn't that joke so funny?! {}" # A variable holding a string

print(joke_evaluation.format(hilarious)) # Printing both variables

w = "This is the left side of..." # A variable
e = "a string with a right side." # A variable

print(w + e) # Printing both variables

# There are four strings inside a string

# Using the + makes a string longer because it adds both the variables which contain a string
