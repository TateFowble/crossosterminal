import os, webbrowser, platform, json, sys
from time import sleep
from helpCommands import help
from logo import logo
from makeSpace import spaced
from randomGenerator import randomGen
from youKnow import I_Know
from sike8Ball import sike8

platformType = platform.platform()

valuedLogo = 4

def main(a):

    spaced(500)
    logo(valuedLogo)
    spaced(5)
    print('Running ' + platformType)
    spaced(1)
    print('Type \'help\' for a list of commands')
    spaced(2)
    if(a):
        while(a):
            spaced(1)

            firstCommand = input('> ')

            spaced(1)

            if(firstCommand == 'help' or firstCommand == 'Help' or firstCommand == 'HELP'):
                spaced(2)
                help()
                spaced(2)
            
            elif(firstCommand == 'gui' or firstCommand == 'Gui' or firstCommand == 'GUI'):
                webpage = "index.html"
                webbrowser.get('firefox').open(webpage)
                webbrowser.get('chrome').open(webpage)
                os.system('start ' + webpage)

                if(webbrowser.Error()):
                    print('Error: Could not launch applet')
                else:
                    print('Launched')

            elif(firstCommand == 'I know'):
                I_Know()
            elif(firstCommand == 'sike8' or firstCommand == 'Sike8' or firstCommand == 'SIKE8'):
                spaced(2)
                sike8()
                spaced(2)

            elif (firstCommand == 'random' or firstCommand == 'Random' or firstCommand == 'RANDOM'):
                spaced(1)
                randomGen()
                spaced(1)

            elif(firstCommand == 'hackermode' or firstCommand == 'Hackermode' or firstCommand == 'HACKERMODE'):
                print('Function stills to be written')


            elif(firstCommand == 'logo' or firstCommand == 'Logo' or firstCommand == 'LOGO'):
                spaced(10)
                logo(valuedLogo)

            elif(firstCommand == 'clear' or firstCommand == 'Clear' or firstCommand == 'CLEAR'):
                spaced(300)

            elif(firstCommand == 'exit' or firstCommand == 'Exit' or firstCommand == 'EXIT'):
                spaced(2)
                print('Entering normal terminal mode')
                spaced(2)
                a = False
                exit
            else:
                print('Command Unrecognized')
    
    else:
        spaced(2)
        print('Entering normal terminal mode')
        spaced(2)
        exit

main(True)
