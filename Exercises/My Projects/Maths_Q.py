#Maths Questionnaire Game
print ("Welcome to the maths questionnaire")
username = input("Please enter your username:")
print("Welcome " + username)
count = 0

def question(question, answer, current_count):
    if int(input(question)) == answer:
        print("Well done")
        current_count = current_count + 1
    else:
        print("Incorrect")
   # print (f"Your score is: {current_count}")
    return current_count

count = question("1. What's 3x3?", 9, count)
count = question("2. What's 9x4?", 36, count)  
count = question("3. What's 6x6?", 36, count) 
count = question("4. What's 7x7?", 49, count) 
count = question("5. What's 10x10?", 100, count)
count = question("6. What's 5x3?", 15, count) 
count = question("7. What's 4x7?", 28, count) 
count = question("8. What's 8x9?", 72, count)
count = question("9. What's 6x4?", 24, count) 
count = question("10. What's 1x0?", 0, count)
print("Congratulations! Your final score is", count)