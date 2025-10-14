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

        #takes the value from auto click settings (ordered same as UI) and parses through functions to update value in AutoClicker class
        self.clickingMethodInput.currentTextChanged.connect(self.update_clicking_method)
        self.clickDelayInput.valueChanged.connect(self.update_click_delay)
        self.startDelayInput.valueChanged.connect(self.update_start_delay)

        #todo: find function to get updated keybinds from UI
        #todo: find best output box to show CPS


    #stock standard crap right here
    def update_click_delay(self, value):
        self.clicker.set_click_delay(value)

    def update_start_delay(self, value):
        self.clicker.set_start_delay(value)

    def update_clicking_method(self, method:str):
        self.clicker.set_click_method(method)
        if method == "Left Click":
            self.clicker.set_click_method(method)
        elif method == "Right Click":
            self.clicker.set_click_method(method)
        elif method == "Middle Click":
            self.clicker.set_click_method(method)


class ClickerThread(QThread):
    def __init__(self, clicker):
        super().__init__()
        self.clicker = clicker

    def run(self):
        self.clicker.start_clicker()
