import random


def randomGen(LowestN = 0,HighestN=10):
    print('Leave blank for default numbers to be used; 1 to 10')
    
    LowestN = input('Min Number: ')
    HighestN = input('Max Number: ')

    if (str(LowestN) or str(HighestN)):
        LowestNum = int(LowestN)
        HighestNum = int(HighestN)
        randomNum = random.randint(LowestNum, HighestNum)
        print('')
        print('')
        print(''*5, randomNum)

    elif(str(LowestN) or str(HighestN)):
        print('Error: Use numerial value')

    else:
        randomNum = random.randint(1, 10)
        print('')
        print('')
        print(''*5, randomNum)

#randomGen()
