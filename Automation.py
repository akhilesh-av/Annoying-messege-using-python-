"""
This is code for anoying anyone or automate the messege at a number of times in a digital space
This code will work when you run the code on an ide then where you click "Enter" , (Triger of the code is Enter Button in keyboard)
"""

import pyautogui as pg
import time

print("This code will run when you click on Enter Button in keyboard")  # giving intication to user
print("run in 5 Sec ")   # giving intication to user
time.sleep(5)


for i in range(100):            #code will run 100 time , means on click of "Enter" it send 100 time . 
    pg.write("What ever you want to write for 100 time ")
    time.sleep(0.5)
    pg.press("Enter")    #OnClick of "Enter" button message send 100 time on where you click   