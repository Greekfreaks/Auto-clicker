import threading
import time
import keyboard
import pyautogui
from pyautogui import click
from collections import deque


class AutoClicker:
    def __init__(self):
        #loop variables
        self.clicking = False
        self.running = True
        self.exit_requested = False

        self.clickDelay = .5
        self.startDelay = .5
        self.clickingMethod = 'Right Click'
        self.clickType = 'Single Click'  # Single, Double, or Hold
        self.holdDuration = 0.5  # Duration in seconds for hold click

        self.startClickKey = 's'
        self.stopClickKey = 'x'
        self.exitClickKey = 'q'

        # CPS tracking
        self.click_timestamps = deque(maxlen=100)  # Store last 100 click timestamps
        self.cps_callback = None  # Callback function to update GUI
        self.last_cps_update = time.time()
        self.cps_update_interval = 0.1  # Update CPS every 100ms

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

    def perform_click(self, button='left'):
        """Perform a click based on the current click type"""
        if self.clickType == 'Single Click':
            if button == 'left':
                pyautogui.leftClick()
            elif button == 'middle':
                pyautogui.middleClick()
            elif button == 'right':
                pyautogui.rightClick()
        elif self.clickType == 'Double Click':
            if button == 'left':
                pyautogui.leftClick(clicks=2)
            elif button == 'middle':
                pyautogui.middleClick(clicks=2)
            elif button == 'right':
                pyautogui.rightClick(clicks=2)
        elif self.clickType == 'Hold Click':
            if button == 'left':
                pyautogui.mouseDown(button='left')
                time.sleep(self.holdDuration)
                pyautogui.mouseUp(button='left')
            elif button == 'middle':
                pyautogui.mouseDown(button='middle')
                time.sleep(self.holdDuration)
                pyautogui.mouseUp(button='middle')
            elif button == 'right':
                pyautogui.mouseDown(button='right')
                time.sleep(self.holdDuration)
                pyautogui.mouseUp(button='right')

    def left_click(self):
        delay_flag = False
        while self.running:
            if not delay_flag:
                time.sleep(self.startDelay)
                delay_flag = True
            if self.clicking:
                self.perform_click('left')
                self.record_click()
                print("Click!")
            time.sleep(self.clickDelay)

    def middle_click(self):
        delay_flag = False
        while self.running:
            if not delay_flag:
                time.sleep(self.startDelay)
                delay_flag = True
            if self.clicking:
                self.perform_click('middle')
                self.record_click()
                print("Click!")
            time.sleep(self.clickDelay)

    def right_click(self):
        delay_flag = False
        while self.running:
            if not delay_flag:
                time.sleep(self.startDelay)
                delay_flag = True
            if self.clicking:
                self.perform_click('right')
                self.record_click()
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

    def set_click_type(self, click_type:str):
        print(f"Click type set to: {click_type}")
        self.clickType = click_type

    def set_hold_duration(self, duration:int):
        print(f"Hold duration set to: {duration}ms")
        self.holdDuration = duration / 1000  # Convert to seconds

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

    def set_cps_callback(self, callback):
        """Set the callback function to update CPS in the GUI"""
        self.cps_callback = callback

    def record_click(self):
        """Record a click timestamp and update CPS if needed"""
        current_time = time.time()
        self.click_timestamps.append(current_time)

        # Update CPS if enough time has passed
        if current_time - self.last_cps_update >= self.cps_update_interval:
            self.update_cps()
            self.last_cps_update = current_time

    def update_cps(self):
        """Calculate current CPS and call the callback"""
        if not self.cps_callback:
            return

        current_time = time.time()
        # Remove timestamps older than 1 second
        while self.click_timestamps and current_time - self.click_timestamps[0] > 1.0:
            self.click_timestamps.popleft()

        # Calculate CPS based on clicks in the last second
        cps = len(self.click_timestamps)
        self.cps_callback(cps)

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