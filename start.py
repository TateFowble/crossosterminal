import platform, os

platformType = platform.system()

if (platformType == 'Darwin'):
    os.startfile('main.py')

elif (platformType == 'Windows'):
    os.startfile('main.py')

elif (platformType == 'Linux'):
    os.startfile('main.py')

else:
    print('Error: Unknown operating system')
