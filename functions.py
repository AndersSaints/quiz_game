import questionsdb
import variables
import random
import time
import sys


"""Variables"""

def lets_wait(phrase, t):
    """Implements a pause with dots"""
    print("\n\n %s" % phrase)
    sys.stdout.flush()
    for i in range(t):
        print("."),
        time.sleep(1)
        sys.stdout.flush()


def intro_question(lvl):
    """Generates introduction to the new question"""
    lvl += 1
    sco = variables.score[lvl]
    v = [0 for i in range(9)]
    v[0] = "Here is question #%s worth %s points." % (lvl, sco)
    v[1] = "We're going to question #%s for you to win %s points." % (lvl, sco)
    v[2] = "Question #%s for %s points now." % (lvl, sco)
    v[3] = "This is the turn of question #%s that will get you %s points." % (lvl, sco)
    v[4] = "Now it is the turn of question #%s. Win %s points!" % (lvl, sco)
    v[5] = "Want %s points? Let's see how you can cope with question #%s!" % (sco, lvl)
    v[6] = "Let's see how much time it'll take you to answer question #%s and win %s points!" % (lvl, sco, )
    v[7] = "Now onto question #%s. It is worth %s points." % (lvl, sco)
    v[8] = "Want go win %s points? Here's question #%s." % (sco, lvl)
    n = int(random.random() * 9)
    return v[n]


def ask_question(lvl):
    """Generates a number and gets the question from the database"""
    to_return = "\n " + intro_question(lvl) + "\n "
    to_return += "=" * (len(to_return) - 3) + "\n "
    qnum = int(random.random() * 10)

    global q
    q = questionsdb.get_question(lvl, qnum)
    to_return += q[0]
    to_return += "\n A. " + q[1]
    to_return += "\n B. " + q[2]
    to_return += "\n C. " + q[3]
    to_return += "\n D. " + q[4]

    global correct_answer
    correct_answer = q[5]
    return to_return


def check_answer(lvl):
    """Checks the answer"""
    answer = input("\n You: ").lower()
    global correct_answer, q

    if not (answer in variables.acceptable_answers):  # Checking if the input makes sence
        print("\n I don't understand what you mean. Enter the answer letter, or 'finish' to exit the game.")
        check_answer(lvl)

    elif answer == "finish":
        print(f"\n You chose to finish the game, {variables.player}. You got {variables.score[lvl]} points. Congratulations!")
        quit()

    elif answer == "a" or answer == "b" or answer == "c" or answer == "d":
        if correct_answer == q[ord(answer) - 96]:
            if lvl == 14:
                print(f" ******* CONGRATULATIONS, {variables.player.upper()}! *************")
                print(f" **********  YOU GOT {variables.score} POINTS! *************")
                print(" You reached the top! This was an excellent game! Once again, congratulations!")
            else:
                print(f"\n You got it right, {variables.player}!\n\
                       Let's proceed to question #{lvl + 2}!")
                print(ask_question(lvl + 1))
                check_answer(lvl + 1)

        else:
            print(f"\n Oops. The answer you chose is incorrect.\n The right answer is {correct_answer}.")
            print(" Thank you for the game!")

            while True:
                user_choice = input("\n\n Would you like to to try one more time? (y/n)  ")
                if user_choice.lower() in ("y", "yes"):
                    print(ask_question(0))
                    check_answer(0)
                elif user_choice.lower() in ("n", "no"):
                    print(" Thank you for playing!")
                    quit()
                else:
                    print("\n I don't understand what you mean. Enter 'yes' to keep playing, or 'no' to exit the game.")
