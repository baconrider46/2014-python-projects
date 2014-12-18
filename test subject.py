
print("====================================================================")
print("11       1111111   111111   111111    1111111  11        1   111111                             ")
print("11       1     1  1      1  1     1      1     1 1       1  1                                   ")
print("11       1     1  1      1  1      1     1     1   1     1  1                                   ")
print("11       1     1  11111111  1      1     1     1    1    1  1    111                            ")
print("11       1     1  1      1  1      1     1     1     1   1  1      1                            ")
print("11       1     1  1      1  1      1     1     1      1  1  1      1                            ")
print("11       1     1  1      1  1     1      1     1       1 1  1     1                             ")
print("1111111  1111111  1      1  111111    1111111  1        11  111111                              ")
print("====================================================================")


print('Welcome test subject.')
name = 'Test Subject 237'

print("answer these questions for your freedome " + name)
def q1():
    print("where does pizza originate from?")
    answer = input('> ')

    if answer == 'Germany':
        print("RRRRRR...Wrong try again.")
        return False
    elif answer == 'Italy':
        print("Dinnnnggggg...Correct.")
        return True
    else:
        print('RRRRRR...Wrong try agian.')
        return False

def q2():
    print("Does Bear Grills like pee?")
    answer = input('> ')
    
 
    if answer == 'no':
        print("RRRRRR...Wrong try again.")
        return False
    elif answer == 'yes':
        print("Dinnnnggggg...Correct.")
        return True
    else:
        print("RRRRRR...Wrong try again.")
        return False

def q3():
    print("How many blocks of iron does it take to make a anvil in minecraft")
    answer = input('> ')
    
    if answer == '2':
        print("RRRRRR...Wrong try again.")
        return False
    elif answer == '3':
        print("Dinnnnggggg...Correct.")
        return True
    else:
        print("RRRRRR...Wrong try agian.")
        return False

questions = [q1, q2, q3]
import random

while questions:
    question = random.choice(questions)
    correct = question()
    if correct:
        questions.remove(question)

