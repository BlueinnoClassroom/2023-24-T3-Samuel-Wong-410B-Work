import pyautogui as gui
from PIL import ImageGrab
import time
gui.PAUSE = 0
# gui.displayMousePosition()

left = 890
top = 322
right = 940
bottom = 355

# time.sleep(1)
# screenshot = ImageGrab.grab(
#     bbox = (left, top, right, bottom)
# )
# screenshot.save('sad.png')
while True:
    screenshot = ImageGrab.grab(
        bbox = (left, top, right, bottom)
    )
    screenshot.save('sad.png')
    pixels = screenshot.load()              

    has_green = False
    for x in range(screenshot.width):
        for y in range(screenshot.height):
            px = pixels[x, y]
            if px[1] > 100:
                print(px)
                has_green = True
                break

    if has_green:
        gui.press('space')

