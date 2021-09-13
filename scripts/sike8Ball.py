import random
from makeSpace import spaced

def sike8():
    spaced(1)
    user123 = str(input('Ask a question: '))
    spaced(1)
    randomNum = random.randint(1,20)
    print(randomNum)
    if(randomNum == 1):
        print('As I see it, yes.')
    elif(randomNum == 2):
        print('Ask again later.')
    elif(randomNum == 3):
        print('Better not tell you now.')
    elif(randomNum == 4):
        print('Cannot predict now.')
    elif(randomNum == 5):
        print('Concentrate and ask again.')
    elif(randomNum == 6):
        print('Don\'t count on it.')
    elif(randomNum == 7):
        print('It is certain.')
    elif(randomNum == 8):
        print('It is decidely so.')
    elif(randomNum == 9):
        print('Most likely.')
    elif(randomNum == 10):
        print('My reply is no.')
    elif(randomNum == 11):
        print('My sources say no.')
    elif(randomNum == 12):
        print('Outlook not so good.')
    elif(randomNum == 13):
        print('Outlook good.')
    elif(randomNum == 14):
        print('Reply hazy, try again')
    elif(randomNum == 15):
        print('Signs point to yes')
    elif(randomNum == 16):
        print('Very doubtful')
    elif(randomNum == 17):
        print('Without a doubt')
    elif(randomNum == 18):
        print('Yes')
    elif(randomNum == 19):
        print('Yes - definitely')
    elif(randomNum == 20):
        print('You may rely on it')
