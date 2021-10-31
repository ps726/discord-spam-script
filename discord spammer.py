from os import times
import time

time.sleep(5)

from subprocess import run
import keyboard
from pynput.keyboard import *

proggramver = (int(0))
running = (bool(True))

keyboard = Controller()

keyboard.type("hello world")

def say(word):
    time.sleep(0.5)
    keyboard.type(word)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

while running == True:
    say("when the imposter is sus")
