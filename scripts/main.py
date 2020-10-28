import os, webbrowser, platform, json, sys
from time import sleep
from helpCommands import help
from logo import logo
from makeSpace import spaced

platformType = platform.platform()

def main(a):

    spaced(500)
    logo()
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

            if(firstCommand == 'help'):
                help()
            
            elif(firstCommand == 'gui'):
                webpage = "index.html"
                webbrowser.get('firefox').open(webpage)
                webbrowser.get('chrome').open(webpage)
                os.system('start ' + webpage)

                if(webbrowser.Error()):
                    print('Error: Could not launch applet')
                else:
                    print('Launched')

            elif(firstCommand == 'hackermode'):
                print('Function stills to be written')


            elif(firstCommand == 'logo'):
                spaced(10)
                logo()

            elif(firstCommand == 'clear'):
                spaced(300)

            elif(firstCommand == 'exit'):
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
