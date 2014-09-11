import random


print('oh ya dawg ask me any question in the world and i will answer! ')


answers = ['yes.','oh yaaaa boyeeeee!.','No..','your friend would know.','well you shall see','ask your mom','nobo]


while True:
    print('give me your question')
    question = input('> ')
    answer = random.choice(answers)     
    print(answer)
