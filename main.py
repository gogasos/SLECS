import time
import pyautogui


pyautogui.keyDown('alt')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.keyUp('alt')
time.sleep(1)

while True:

    pyautogui.click(x=2322, y=1000)  
    time.sleep(60)  
    
    pyautogui.click(x=2322, y=585) 
    time.sleep(10)
