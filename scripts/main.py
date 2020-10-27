import os, webbrowser, platform, json
from time import sleep

platformType = platform.platform()
def main(a = False):

    spaced(500)
    logo()
    spaced(5)
    print('Type \'help\' for a list of commands')
    spaced(2)
    if(a):
        while(a):
            print('running ' + platformType)
            spaced(1)
            firstCommand = input('> ')
            spaced(1)
            if(firstCommand == 'help'):
                help()
            
            elif(firstCommand == 'gui'):
                webpage = "index.html"
                webbrowser.get('firefox').open(webpage)
                os.system('open ' + webpage)

                if(webbrowser.Error()):
                    print('Error: Could not launch applet')

            elif(firstCommand == 'hackermode'):
                print('Function stills to be written')


            elif(firstCommand == 'logo'):
                logo()

            elif(firstCommand == 'clear'):
                spaced(5000)

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


def help():
    spaced(2)
    print('-'*50)
    print('Help  -  Let\'s the user know of the availible commands')
    print('GUI  -  Displays a GUI version of the program in a web browser')
    print('Hackermode  -  Displays random bytecode to simulate movie hacking')
    print('Logo  -  Displays the program\'s logo')
    print('Clear  -  Clears the terminal screen while program is running')
    print('Exit  -  Exits the program entirely')
    print('-'*50)
    spaced(2)


def spaced(howMany):
    for howMany in range(0, howMany):
        print('')

def logo():
    print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    print('- '*50)
    print(' -'*50)
    print('- '*50)
    print(' -'*50)
    print('- '*50)
    print(' -'*50)
    print('- '*50)
    print(' -'*50)
    print('- '*50)
    print(' -'*50)
    print('- '*50)
    print(' -'*50)
    print('- '*50)
    print(' -'*50)
    print('- '*50)
    print(' -'*50)
    print('- '*50)
    print(' -'*50)
    print('- '*50)

main(True)