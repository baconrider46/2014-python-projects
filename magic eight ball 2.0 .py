import random

answers = ['yes.',
          'Would not wanna ruin the suprise',
          'no.',
          'Maybe.',
          ':(']
           


print("Hello Dwarf Whats Your Question")


while True:
    question = input('> ')
    answer = random.choice(answers)
    
    print(answer)
