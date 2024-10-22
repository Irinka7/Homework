import random

def button ():

    answer , answer_2 = [] , []
    list_20 = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    gacha = int(random.choice(list_20))

    for i in range (1, len(list_20) + 2):
        for y in range (i + 1, len(list_20) + 1):
            if gacha %  (i + y) == 0:
                answer.append([i , y])

    return f'{answer_2} - {answer}'

print (button())
