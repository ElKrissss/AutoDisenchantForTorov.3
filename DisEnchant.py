import pyautogui
import keyboard
import time
import config


start = list(config.start)
end = config.end
delay = config.delay
gap = config.gap

def suma():
    time.sleep(delay)
    keyboard.press('shift')
    pyautogui.click(end)
    pyautogui.click(end)
    pyautogui.click(end)
    keyboard.release('shift')


time.sleep(3)
def izq():
    slot = 0
    global start
    while slot < 9 :
        keyboard.press('shift')
        pyautogui.click(start)
        keyboard.release('shift')
        slot = slot +1
        time.sleep(delay)
        suma()
        time.sleep(delay)
        if slot < 9:
            start[0] = start[0] -gap 
def der():
    slot = 0
    global start
    while slot < 9 :
        keyboard.press('shift')
        pyautogui.click(start)
        keyboard.release('shift')
        slot = slot +1
        time.sleep(delay)
        suma()
        time.sleep(delay)
        if slot < 9:
            start[0] = start[0] +gap 


izq()
start[1] = start[1] -gap
der()
start[1] = start[1] -gap
izq()
