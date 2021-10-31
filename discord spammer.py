from os import times
import time

#askes the user what they want to spam
userinput = (str(input()))
print("what do you want to spam")

running = (bool(False))

#starts the spamming
if userinput == "hello":
    running == True
    print("spamming starts in 5 seconds")
else:
    running == True
    print("spamming starts in 5 seconds")

#gives you time move you mouse to discord before spamming starts
time.sleep(5)

#spamming part
from subprocess import run
import keyboard
from pynput.keyboard import *

keyboard = Controller()

def say(word):
    time.sleep(0.5)
    keyboard.type(word)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

#loop to keep spamming
while running == True:
    say(userinput)
    
