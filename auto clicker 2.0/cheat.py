import pyautogui as gui
import multiprocessing

# gui.displayMousePosition()

gui.PAUSE = 0.01

main_btn_pos = (570, 427)
upgrade_btn_pos = [
    (955, 315),
    (955, 385),
    (955, 455),
    (955, 521),
    (955, 591)
]

def click_main():
    while True:
        gui.click(main_btn_pos)
 
def click_upgrade():
    while True:
        for x, y in upgrade_btn_pos:
            gui.click(x, y)

def click_yellow_btn():
    while True:
        print('click_yellow_btn')
        try:
            pos = gui.locateCenterOnScreen(
                'yellow_btn.png',
                confidence=0.001
            )
            print('click_yellow_btn: pos', pos)
            gui.click(pos)
        except:
            continue

if __name__ == '__main__':
    main_process = multiprocessing.Process(target=click_main)
    # upgrade_process = multiprocessing.Process(target=click_upgrade)    
    # yellow_process = multiprocessing.Process(target=click_yellow_btn)

    main_process.start()
    # upgrade_process.start()
    # yellow_process.start()
