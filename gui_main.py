from PySide6.QtCore import QThread
from PySide6.QtWidgets import QApplication, QMainWindow
from gui_design import Ui_MainWindow
from clicker_logic import AutoClicker
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.clicker = AutoClicker()
        self.clicker_thread = ClickerThread(self.clicker)
        self.clicker_thread.start()

        #Auto click settings (ordered same as UI)
        self.clickingMethodInput.currentTextChanged.connect(self.update_clicking_method)
        self.clickDelayInput.valueChanged.connect(self.update_click_delay)
        self.startDelayInput.valueChanged.connect(self.update_start_delay)

        #todo: find function to get updated keybinds from UI
        #todo: find best output box to show CPS



    def update_click_delay(self, value):
        print(f"Delay set to {value}")
        self.clicker.set_click_delay(value)

    #todo: I have no clue why these if statements are not executing. printing 'method' shows they are equal (maybe wrong type,way  of parsing value????????)
    def update_start_delay(self, method:str):
        print(f"Start delay set to {method}")
        if method == "Left Click":
            self.clicker.set_click_delay(value)
        elif method == "Right Click":
            print("hi")
            self.clicker.set_click_delay(value)
        elif method == "Middle Click":
            self.clicker.set_click_delay(value)

    def update_clicking_method(self, string):
        print(f"click method set to {string}")
        self.clicker.set_click_method(string)


class ClickerThread(QThread):
    def __init__(self, clicker):
        super().__init__()
        self.clicker = clicker

    def run(self):
        self.clicker.start_clicker()
