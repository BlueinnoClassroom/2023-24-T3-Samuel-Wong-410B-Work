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


def click_cookie():
    try:
        while True:
            gui.click(main_cookie_pos)
    except gui.FailSafeException:
        print(f"Fail-safe triggered")
        return


def click_upgrade():
    try:
        top = 221
        bot = 793

        while True:
            gui.scroll(-10, x=1220, y=412)
            for y in range(bot, top, -20):
                gui.moveTo(1214, y)
                px = gui.pixel(1214 * 2, y * 2)
                print(px)
                print(y)
                while px[0] > 200:
                    px = gui.pixel(1214 * 2, y * 2)
                    for i in range(20):
                        gui.click(1214, y)
            gui.scroll(5, 1214, 412)
            for y in range(bot, top, -20):
                gui.moveTo(1214, y)
                px = gui.pixel(1214 * 2, y*2)
                print(px)
                print(y)
                while px[0] > 200:
                    px = gui.pixel(1214 * 2, y * 2)
                    for i in range(20):
                        gui.click(1214, y)
            

    except gui.FailSafeException:
        print(f"Fail-safe triggered")
        return


def click_golden_cookie():
    while True:
        try:
            pos = gui.locateCenterOnScreen("golden_cookie.png", confidence=0.45)
            print("click_golden_cookie: pos", pos)
            gui.click(pos.x/2, pos.y/2)
        except gui.FailSafeException:
            print(f"Fail-safe triggered") 
            return
        except:
            print('error finding gold cookie')
            continue

def read_data():
    try:
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
    except gui.FailSafeException:
        print(f"Fail-safe triggered")
        return


def main():
    click_cookie_process = multiprocessing.Process(target=click_cookie)
    click_upgrade_process = multiprocessing.Process(target=click_upgrade)
    click_golden_cookie_process = multiprocessing.Process(target=click_golden_cookie)
    read_data_process = multiprocessing.Process(target=read_data)

    processes = [
        # click_cookie_process,
        click_upgrade_process,
        # click_golden_cookie_process,
        # read_data_process,
    ]

    for process in processes:
        process.start()

    try:
        # Wait for all processes to complete (in this case, they run indefinitely)
        for process in processes:
            process.join()
    except KeyboardInterrupt:
        print("Manual interruption detected. Terminating all processes.")
        for process in processes:
            process.terminate()


if __name__ == "__main__":
    main()
