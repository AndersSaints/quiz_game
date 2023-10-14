

from functions import ask_question, check_answer
import variables

print(" *************************************************")
print(" *              //   Welcome to  \\\              *")
print(" *              \\\    MY QUIZ    //              *")
print(" *************************************************\n")

variables.player = input(" What is your name? ")

print(ask_question(0))
check_answer(0)
