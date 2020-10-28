import random



def randomGen(LowestN = 0,HighestN=10):
    print('Leave blank for default numbers to be used; 1 to 10')

    LowestN = int(input('Min Number: '))
    HighestN = int(input('Max Number: '))

    randomNum = random.randint(LowestN, HighestN)
    print(''*5, randomNum)
