import time
from subprocess import run
from typing import Text
from pynput.keyboard import *
import random

messager = (str(random.randint(1,100)))

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

def say_random():
    time.sleep(5)
    while running == True:
        messager = (str(random.randint(1,1000)))
        keyboard.type(messager)
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
