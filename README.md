# SLECS

Simple Last Epoch Connect Script made in python

You can just figure out the X & Y on your screen. 

Adjust any sleep timers to your liking.





## Usage/Examples

pip install pyautogui

(Rember to have Last Epoch on the next Alt + Tab)


then run in vscode as is.

```py
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

```



