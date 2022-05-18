#Maths Questionnaire Game with the help of Robin
import os
os.system("color")
import random
print ("Welcome to the maths questionnaire")
username = input("Please enter your username:")
print("Welcome " + username)
count = 0

def question(question, answer, current_count):
    if (input(question)) == answer:
        print("Well done")
        current_count = current_count + 1
    else:
        print("Incorrect")
   # print (f"Your score is: {current_count}")
    return current_count
questions = ["2+3","5x5","3+200", "7x7", "36/4", "40x25", "55+60", "32+40"]
answers = ["5", "25", "203", "49", "9", "1000", "115", "72"]
for _ in range (5):
    questionnumber = random.randint(0,7)
    count = question(f"What is {questions[questionnumber]}? ",answers[questionnumber], count)
#count = question("2. What's 9x4?", "36", count)  
#count = question("1. What's 3x3?", "9", count)
#count = question("3. What's 6x6?", "36", count) 
#count = question("4. What's 7x7?", "49", count) 
#count = question("5. What's 10x10?", "100", count)
#count = question("6. What's 5x3?", "15", count) 
#count = question("7. What's 4x7?", "28", count) 
#count = question("8. What's 8x9?", "72", count)
#count = question("9. What's 6x4?", "24", count) 
#count = question("10. What's 1x0?", "0", count)
if count >= 3:
    print(f"\033[36mCongratulations\033[0m \033[5m\033[32m{username}\033[0m! Your final score is\033[44m", count,"\033[0m")
else:
    print(f"Better luck next time {username} Your score is", count)