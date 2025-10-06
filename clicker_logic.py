import threading
import time
import keyboard
import pyautogui


class AutoClicker:
    def __init__(self):
        self.clicking = False
        self.running = True

        self.clickDelay = 100
        self.startDelay = 100
        self.clickingMethod = 'Right Click'

        pyautogui.PAUSE = 0 #remove default delay between clicks, this using the sleep class instead

    def key_listener(self):
        while self.running:
            if keyboard.is_pressed('s'):
                self.clicking = True
            elif keyboard.is_pressed('x'):
                self.clicking = False
            elif keyboard.is_pressed('q'):
                self.running = False
            time.sleep(0.05)

    def left_click(self):
        while self.running:
            if self.clicking:
                pyautogui.leftClick()
                print("Click!")
            time.sleep(0.008)

    def middle_click(self):
        while self.running:
            if self.clicking:
                pyautogui.rightClick()
                print("Click!")
            time.sleep(0.008)

    def right_click(self):
        while self.running:
            if self.clicking:
                pyautogui.middleClick()
                print("Click!")
            time.sleep(self.clickDelay)

    def set_click_delay(self, value):
        self.clickDelay = value


    def start_clicker(self):
        listener_thread = threading.Thread(target=self.key_listener, daemon=True)
        listener_thread.start()
        self.left_click()