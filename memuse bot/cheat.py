import pyautogui as gui
from PIL import ImageGrab
import numpy as np
import time

gui.PAUSE = 0
# gui.displayMousePosition()

left = 566
right = 873
top = 700
bottom = 713

keys = ["s", "d", "f", "space", "j", "k", "l"]
div_width = (right - left) / len(keys)

time.sleep(2)
zone_img = ImageGrab.grab(bbox=(left, top, right, bottom))
# zone_img.save("zone_img.png")

empty_divs = []
for i in range(len(keys)):
    start_x = i * div_width
    end_x = (i + 1) * div_width

    div = zone_img.crop((start_x, 0, end_x, zone_img.height))
    # div.save(f"div_{i}.png")

    gray_div = div.convert("L")
    # gray_div.save(f"gray_div_{i}.png")

    px = np.array(gray_div)
    empty_divs.append(px)

print("You may start the game now!")
while True:
    latest_img = ImageGrab.grab(bbox=(left, top, right, bottom))

    latest_divs = []
    for i in range(len(keys)):
        start_x = i * div_width
        end_x = (i + 1) * div_width

        div = latest_img.crop((start_x, 0, end_x, zone_img.height))

        gray_div = div.convert("L")

        px = np.array(gray_div)
        latest_divs.append(px)

    for i in range(len(keys)):
        img1 = empty_divs[i]
        img2 = latest_divs[i]

        diff = img1.astype("float") - img2.astype("float")
        diff = np.sum(diff**2)
        diff /= float(img1.shape[0] * img2.shape[1])

        if diff > 2150:
            gui.keyDown(keys[i])
        else:
            gui.keyUp(keys[i])