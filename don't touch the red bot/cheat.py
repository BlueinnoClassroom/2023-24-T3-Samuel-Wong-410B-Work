import pyautogui as gui
from PIL import ImageGrab

gui.PAUSE = 0.0127

# gui.displayMousePosition()

x1 = 1056
x2 = 1314
x3 = 1572
x4 = 1826
y = 1260

while True:
    screenshot = ImageGrab.grab()
    pixels = screenshot.load()
    p1 = pixels[x1, y]
    p2 = pixels[x2, y]
    p3 = pixels[x3, y]
    p4 = pixels[x4, y]
    if p1[1] > 200:
        gui.press('h')
    elif p2[1] > 200:
        gui.press('j')
    elif p3[1] > 200:
        gui.press('k')
    elif p4[1] > 200:
        gui.press('l')