import threading
import time
import keyboard
import pyautogui

clicking = False
running = True

pyautogui.PAUSE = 0 #remove default delay between clicks, this using the sleep class instead

def key_listener():
    global clicking, running
    while running:
        if keyboard.is_pressed('s'):
            clicking = True
        elif keyboard.is_pressed('x'):
            clicking = False
        elif keyboard.is_pressed('q'):
            running = False
        time.sleep(0.05)

def auto_clicker():
    global clicking, running
    while running:
        if clicking:
            pyautogui.leftClick()
            print("Click!")
        time.sleep(0.008)

listener_thread = threading.Thread(target=key_listener, daemon=True)
listener_thread.start()
auto_clicker()
