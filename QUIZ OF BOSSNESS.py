print('Welcome to my Swager quiz game')
name = 'Traveler'

print("answer these questions to pass the gate of knoledge " + name)
def q1():
    print("what Does the fox say?")
    answer = input('> ')

    if answer == 'wawawawa':
        print("Ummm no Go back to youtube")
        return False
    elif answer == 'hahahanayayya':
        print("Heck Nah YOU STUPID")
        return False
    elif answer == 'nahnahnah':
        print("FINALLY YES YOUR NOT STUPID")
        return True
    else:
        print('NO YOU STOOPED')
        return False

def q2():
    print("what is my name")
    answer = input('> ')
       
    if answer == 'Rob':
        print("No")
        return False
    elif answer == 'Nic':
        print("Hahahahahhaha... no")
        return False
    elif answer == 'Aidan':
        print("Yess")
        return True

questions = [q1, q2]
import random

while questions:
    question = random.choice(questions)
    correct = question()
    if correct:
        questions.remove(question)
