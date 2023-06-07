import pyautogui
import keyboard
import time
import config

stealcoords = config.stealc
dumpcoords = config.dumpc
panickey = config.panickey

delay = 4
loop = True

def parar(e):
    global loop
    loop = False

keyboard.on_press_key(panickey, parar)

time.sleep(3)
while loop == True:
    time.sleep(delay)
    pyautogui.click(stealcoords)
    pyautogui.click(stealcoords)
    time.sleep(delay)
    pyautogui.click(dumpcoords)
    pyautogui.click(dumpcoords)
    time.sleep(delay)


    
 
