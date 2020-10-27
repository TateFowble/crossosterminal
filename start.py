import platform, os

platformType = platform.system()

if (platformType == 'Darwin'):
    os.startfile('start.py')

elif (platformType == 'Windows'):
    os.startfile('start.py')

elif (platformType == 'Linux'):
    os.startfile('start.py')

else:
    print('Bro idk')
