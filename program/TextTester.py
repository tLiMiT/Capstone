
from TextInserter import *
from MessageSender import *
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def binaryChoice():
    while True:
        temp = raw_input('')
        if (temp[0]).lower() == 'a':
            return True
        elif (temp[0]).lower() == 's':
            return False

def printBinaryControls(ml, mr):
    print '(A = ' + ml + '\tS = ' + mr + ')'

def letterFilter(letter):
    if letter == ' ':
        return '_'
    else:
        return letter


def printChoices(choices):
    print 'Left\tRight'
    for c in sorted(choices.items()):
        if c[1] == True:
            print letterFilter(c[0])
        elif c[1] == False:
            print '\t' + letterFilter(c[0])


def textInserter_messageSender_TestHarness():
    clear()
    selector = ChoicePath(huffmanAlgorithm(LETTER_FREQ))
    message = ''
    prompt = 'Enter a text message'
    
    menu_options = ['Add Letter', 'Backspace', 'Cancel', 'Done']
    option_counter = 0
    temp = ''
    
    while(True):
        clear()
        print prompt + '\n'
        print 'Current message\t ->' + message + '<-'
        print 'Options:'
        for index in range(len(menu_options)):
            if index == option_counter:
                temp = '->\t'
            else:
                temp = '\t'
            print temp + menu_options[index]
        printBinaryControls('select', 'shift')
        # Input
        if binaryChoice():
            # Selects option
            if option_counter == 0:
                #Runs Huffman Letter Selector
                while selector.getChoiceCount() >1:
                    clear()
                    printChoices(selector.splitChoices())
                    printBinaryControls('select left column','select right column')
                    selector.select(binaryChoice())
                message = message + selector.getChoices()[0]
                selector.reset()
            elif option_counter == 1:
                message = message[:-1]
            elif option_counter == 2:
                return
            elif option_counter == 3:
                sendMessage(number,message)
                return message
            else:
                pass
        else:
            option_counter += 1
            option_counter %= len(menu_options)


textInserter_messageSender_TestHarness()
