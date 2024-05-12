import keyboard
import pyautogui
import time
import os
import mouse
from PIL import Image, ImageGrab
import pytesseract
import numpy as np
import sys
import subprocess

pages = int(input("Enter the number of pages in the document: "))

os.system("notify-send \"Put your cursor at the top left of your document\" -t 6000")
time.sleep(1)
count = 5
while count != 0:
    os.system(f"notify-send \"{count}\"... -t 1000")
    count -= 1
    time.sleep(1)
top_left = mouse.get_position()

os.system("notify-send \"Put your cursor at the bottom right of your document\" -t 6000")
time.sleep(1)
count = 5
while count != 0:
    os.system(f"notify-send \"{count}...\" -t 1000")
    count -= 1
    time.sleep(1)
bottom_right = mouse.get_position()

# time.sleep(2)
# os.system("notify-send \"Put your cursor at the copy icon\" -t 6000")
# time.sleep(1)
# count = 5
# while count != 0:
#     os.system(f"notify-send \"{count}...\" -t 1000")
#     count -= 1
#     time.sleep(1)
# copy_icon_pos = mouse.get_position()
# pyautogui.moveTo(copy_icon_pos)
# time.sleep(.2)
# pyautogui.leftClick()

for i in range(pages):
    time.sleep(0.5)

    # for flameshot applet
    # pyautogui.moveTo(1910,10)
    # pyautogui.leftClick()
    # time.sleep(0.1)
    subprocess.Popen(["flameshot", "gui"])
    pyautogui.moveTo(top_left)
    time.sleep(0.1)
    pyautogui.dragTo(bottom_right, duration=.5)
    pyautogui.hotkey("ctrl", "c")
    # pyautogui.moveTo(copy_icon_pos)
    time.sleep(.2)
    pyautogui.leftClick()
    pyautogui.press("j")

    ImageGrab.grabclipboard().save('/home/adi/Pictures/text.png','PNG')

    filename = '/home/adi/Pictures/text.png'
    img1 = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img1)

    with open(sys.argv[1], "a") as f:
        f.write(text) 
        f.write("\n")
