import threading
import time
import keyboard
import pyautogui
from pyautogui import click


class AutoClicker:
    def __init__(self):
        self.clicking = False
        self.running = True

        self.clickDelay = .5
        self.startDelay = .5
        self.clickingMethod = 'Right Click'

        pyautogui.PAUSE = 0 #remove default delay between clicks, this using the sleep class instead

    def key_listener(self):
        while self.running:
            if keyboard.is_pressed('s'):
                print('start')
                self.clicking = True
            elif keyboard.is_pressed('x'):
                print('stop')
                self.clicking = False
            elif keyboard.is_pressed('q'):
                print('quit')
                self.running = False
            time.sleep(0.1)

    def set_click_method(self, value):
        self.clickingMethod = value
        print(f"Click delay set to {self.clickingMethod}")

    def left_click(self):
        delay_flag = False
        while self.running:
            if not delay_flag:
                time.sleep(self.startDelay)
                delay_flag = True
            if self.clicking:
                pyautogui.leftClick()
                print("Click!")
            time.sleep(self.clickDelay)

    def middle_click(self):
        delay_flag = False
        time.sleep(self.startDelay)
        while self.running:
            if self.clicking:
                pyautogui.rightClick()
                print("Click!")
            time.sleep(self.clickDelay)

    def right_click(self):
        delay_flag = False
        time.sleep(self.startDelay)
        while self.running:
            if self.clicking:
                pyautogui.middleClick()
                print("Click!")
            time.sleep(self.clickDelay)

    def set_click_delay(self, value):
        print(f"Click delay set to {value}ms")
        self.clickDelay = value / 1000

    def set_start_delay(self, value):
        print(f"Click delay set to {value}ms")
        self.startDelay = value / 1000

    def read_click_method(self, method:str):
        print(f"Clicking method set to {method}")
        self.clickingMethod = method

    def start_clicker(self):
        listener_thread = threading.Thread(target=self.key_listener, daemon=True)
        listener_thread.start()
        self.left_click()

