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

        #read the inputted keybinds
        self.startKeyInput.keySequenceChanged.connect(self.update_start_key)
        self.startKeyInput.setKeySequence('S')
        self.stopKeyInput.keySequenceChanged.connect(self.update_stop_key)
        self.stopKeyInput.setKeySequence('X')
        self.exitKeyInput.keySequenceChanged.connect(self.update_exit_key)
        self.exitKeyInput.setKeySequence('Q')

        #todo: find best output box to show CPS


    #following 3 functions on parsing value taken from the click settings in UI
    def update_click_delay(self, value):
        self.clicker.set_click_delay(value)

    def update_start_delay(self, value):
        self.clicker.set_start_delay(value)

    def update_clicking_method(self, method:str):
        self.clicker.set_click_method(method)

    #following functions are responsible for reading keybinds (in order of UI)
    def update_start_key(self, sequence):
        keystrokes = sequence.toString().lower()
        self.clicker.set_start_key(keystrokes)

    def update_stop_key(self, sequence):
        keystrokes = sequence.toString().lower()
        self.clicker.set_stop_key(keystrokes)

    def update_exit_key(self, sequence):
        keystrokes = sequence.toString().lower()
        self.clicker.set_exit_key(keystrokes)


class ClickerThread(QThread):
    def __init__(self, clicker):
        super().__init__()
        self.clicker = clicker

    def run(self):
        self.clicker.start_clicker()
