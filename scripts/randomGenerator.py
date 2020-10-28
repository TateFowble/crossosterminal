import random



def randomGen(LowestN = 0,HighestN=10):
    print('Leave blank for default numbers to be used; 1 to 10')
    
    LowestN = int(input('Min Number: '))
    HighestN = int(input('Max Number: '))

    if (LowestN and HighestN == 0):
        randomNum = random.randint(0, 10)
        print('')
        print('')
        print(''*5, randomNum)
    else:
        randomNum = random.randint(LowestN, HighestN)
        print('')
        print('')
        print(''*5, randomNum)
        
    # except (LowestN or HighestN == 0 or str):
    #     print(LowestN)
    #     print('Testing')

