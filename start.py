import platform, os

platformType = platform.system()

if (platformType == 'Darwin'):
    os.system('python3 ./scripts/main.py')

elif (platformType == 'Windows'):
    os.startfile('.\\scripts\\main.py')

elif (platformType == 'Linux'):
    os.system('python3 ./scripts/main.py')

else:
    print('Error: Unknown operating system')