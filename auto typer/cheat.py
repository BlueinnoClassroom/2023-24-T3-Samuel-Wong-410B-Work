import pyautogui as gui
from PIL import ImageGrab
import pytesseract
import time

# gui.displayMousePosition()

left = 734
right = 1411
top = 340
bottom = 377


# # Wait 5 second before start typing
# for i in range(5):
#     print(5 - i)
#     time.sleep(1)

gui.click(left, top - 50)

FILE_NAME = 'word.png'
screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
screenshot.save(FILE_NAME)

height = (bottom - top) + 15
top += height
bottom += height

while True:
    print('extracting text')
    text = pytesseract.image_to_string(FILE_NAME, lang='eng')
    print(text)

    gui.typewrite(text)
    gui.typewrite(' ')
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    screenshot.save(FILE_NAME)
