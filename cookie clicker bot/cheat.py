from PIL import ImageGrab
import pyautogui as gui
import pytesseract
import multiprocessing
import time

# gui.displayMousePosition()

gui.PAUSE = 0

main_cookie_pos = (223, 455)

building_btn_x = 1265
first_building_btn_y = 355
second_building_btn_y = 410

upgrade_btn_y = 241
first_upgrade_btn_x = 1168
second_upgrade_btn_x = 1230


def click_main():
    while True:
        gui.click(main_cookie_pos)


def click_upgrade():
    while True:
        left = 1225
        right = 1438
        up = 360
        height = 18
        for i in range(5):
            screenshot = ImageGrab.grab(bbox=(left, up + height * i, right, up + height * (i + 1))).convert(
            "L"
            )  # to grayscale
            screenshot.save(f"price_of_building {i}.png")

            result = ""
            text: str = pytesseract.image_to_string("number_of_cookies.png", lang="eng")
            for char in text:
                if char.isdigit():
                    result += char

            try:
                result = int(result)
                print(result)
            except Exception as e:
                print(f"error: {e}")
            
        
        


def click_golden_cookie():
    while True:
        try:
            pos = gui.locateCenterOnScreen("golden_cookie.png", confidence=0.001)
            print("click_golden_cookie: pos", pos)
            gui.click(pos)
        except:
            continue


def read_data():
    while True:
        screenshot = ImageGrab.grab(bbox=(0, 225, 430, 265)).convert(
            "L"
        )  # to grayscale
        screenshot.save("number_of_cookies.png")

        result = ""
        text: str = pytesseract.image_to_string("number_of_cookies.png", lang="eng")
        for char in text:
            if char.isdigit():
                result += char

        try:
            result = int(result)
            print(result)
        except Exception as e:
            print(f"error: {e}")

        number_of_cookie = result


if __name__ == "__main__":
    main_process = multiprocessing.Process(target=click_main)
    upgrade_process = multiprocessing.Process(target=click_upgrade)
    yellow_process = multiprocessing.Process(target=click_golden_cookie)
    read_data_process = multiprocessing.Process(target=read_data)

    main_process.start()
    upgrade_process.start()
    yellow_process.start()
    read_data_process.start()
