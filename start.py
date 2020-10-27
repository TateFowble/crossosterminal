import platform, os, subprocess

platformType = platform.system()

if (platformType == 'Darwin'):
    os.startfile('./scripts/main.py')

elif (platformType == 'Windows'):
    os.startfile('.\\scripts\\main.py')

elif (platformType == 'Linux'):
    os.startfile('./scripts/main.py')

else:
    print('Error: Unknown operating system')
