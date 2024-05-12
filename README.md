# OCR : Images to Text
## Introduction
- This python program behaves like an OCR and converts multiple images to text

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
