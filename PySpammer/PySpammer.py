import time
from subprocess import run
from pynput.keyboard import *

keyboard = Controller()

running = (bool(True))

def say(word):
    time.sleep(5)
    while running == True:
        keyboard.type(word)
        time.sleep(0.5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

def paste():
    time.sleep(5)    
    while running == True:
        with keyboard.pressed(Key.ctrl):
            keyboard.press('v')
            keyboard.release('v')
            time.sleep(0.5)
            keyboard.release(Key.ctrl)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
