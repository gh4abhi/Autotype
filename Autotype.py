from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def splitString(words):
    return[char for char in words]

def typeString(words):
    for i in splitString(words):
        keyboard.type(i)
        #time.sleep(.1)
 
words = ''''''
time.sleep(5)
typeString(words)

