# OCR : Images to Text
## Introduction
- This python program behaves like an OCR and converts multiple images to text

## Problem Statement
- Personally, I felt the need to create this program was because of a course I had taken in my 2nd semester of B.Tech. at IIITD
- That course was "Introduction to Sociology and Anthropology" : SOC101
- Instead of a set text book, we used to get extracts from various scholarly texts before every other lecture
- For me, the level of English was sometimes a bit complext to comprehend.
- To combat this situation, I created this program which scanned through those texts and gave me content in text format which I could pipe into chat GPT or windows copilot for them to make it concise and comprehendable.
- Furthermore, I have faced situations where I have an image of some texts, however, I want the content in text format to utilize it further. So, to prevent manually typing the stuff and wasting my time, this program did exactly that in just a couple of minutes depending on the number of pages

## How to Use
- Firstly open the pdf in firefox
- Run the program\
`python3 main.py <file where text should be saved>`
- Point your cursor to the top left of the first page
- Then point your cursor to the bottom right of the first page
- Now, witness the magic!
- Note: It stores the text in the file which you pass as the 1st argument to the program
> [Demo Video](https://youtu.be/GwkooYahCWY)

## Requirements
- Python
    - Keyboard
    - PyAutoGUI
    - Mouse
    - PIL
    - PyTesseract
    - Numpy
- Flameshot (Screenshot utility)

# Note
- This program works only on X11 (Linux), Mac and Windows
- It does not work on wayland because flameshot and pyautogui are not yet natively supported for wayland
- You can try making it work on wayland by running an X server inside wayland using Xwayland even though I was not able to make it work
