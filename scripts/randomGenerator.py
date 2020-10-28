import random



def randomGen(lowestN = 0,HighestN=10):
    print('Leave blank for default numbers to be used')
    def inputed():
        lowestN = input('Min Number: ')
        HighestN = input('Max Number: ')
    int(inputed())
    if(lowestN & HighestN == type(int)):
        randomNum = random.randint(lowestN, HighestN)
        print(randomNum)
    else:
        print('BRO')

