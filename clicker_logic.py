import threading
import time
import keyboard
import pyautogui
from pyautogui import click


class AutoClicker:
    def __init__(self):
        #loop variables
        self.clicking = False
        self.running = True
        self.exit_requested = False

        self.clickDelay = .5
        self.startDelay = .5
        self.clickingMethod = 'Right Click'

        self.startClickKey = 's'
        self.stopClickKey = 'x'
        self.exitClickKey = 'q'

        pyautogui.PAUSE = 0 #remove default delay between clicks, this using the sleep class instead

    def key_listener(self):
        while self.running:
            if keyboard.is_pressed(self.startClickKey):
                print('start')
                self.clicking = True
            elif keyboard.is_pressed(self.stopClickKey):
                print('stop')
                self.clicking = False
            elif keyboard.is_pressed(self.exitClickKey):
                print('quit')
                self.running = False
                self.exit_requested = True
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
        while self.running:
            if not delay_flag:
                time.sleep(self.startDelay)
                delay_flag = True
            if self.clicking:
                pyautogui.middleClick()
                print("Click!")
            time.sleep(self.clickDelay)

    def right_click(self):
        delay_flag = False
        while self.running:
            if not delay_flag:
                time.sleep(self.startDelay)
                delay_flag = True
            if self.clicking:
                pyautogui.rightClick()
                print("Click!")
            time.sleep(self.clickDelay)

    #update values taken from the auto click settings
    def set_click_delay(self, value):
        print(f"Click delay set to {value}ms")
        self.clickDelay = value / 1000

    def set_start_delay(self, value):
        print(f"Click delay set to {value}ms")
        self.startDelay = value / 1000

    def read_click_method(self, method:str):
        print(f"Clicking method set to {method}")
        self.clickingMethod = method

    #udpate keybinds taken from the keybinds menu
    def set_start_key(self, method:str):
        print(f"Start keybind set to: {method}")
        self.startClickKey = method

    def set_stop_key(self, method:str):
        print(f"Stop keybind set to: {method}")
        self.stopClickKey = method

    def set_exit_key(self, method:str):
        print(f"Exit keybind set to: {method}")
        self.exitClickKey = method

    def start_clicker(self):
        listener_thread = threading.Thread(target=self.key_listener, daemon=True)
        listener_thread.start()
        if self.clickingMethod == 'Middle Click':
            self.middle_click()
        elif self.clickingMethod == 'Right Click':
            self.right_click()
        elif self.clickingMethod == 'Left Click':
            self.left_click()
        else:
            print("Invalid clicking method set")
            return 1