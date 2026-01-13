from PySide6.QtCore import QThread, Signal
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

        # Connect exit signal to close the application
        self.clicker_thread.exit_requested.connect(self.close_application)

        # Connect CPS signal to update LCD display
        self.clicker_thread.cps_updated.connect(self.update_cps_display)

        self.clicker_thread.start()

        #takes the value from auto click settings (ordered same as UI) and parses through functions to update value in AutoClicker class
        self.clickingMethodInput.currentTextChanged.connect(self.update_clicking_method)
        self.clickDelayInput.valueChanged.connect(self.update_click_delay)
        self.startDelayInput.valueChanged.connect(self.update_start_delay)

        #connect more settings widgets
        self.clickTypeInput.currentTextChanged.connect(self.update_click_type)
        self.holdDurationSlider.valueChanged.connect(self.update_hold_duration)

        #read the inputted keybinds
        self.startKeyInput.keySequenceChanged.connect(self.update_start_key)
        self.startKeyInput.setKeySequence('S')
        self.stopKeyInput.keySequenceChanged.connect(self.update_stop_key)
        self.stopKeyInput.setKeySequence('X')
        self.exitKeyInput.keySequenceChanged.connect(self.update_exit_key)
        self.exitKeyInput.setKeySequence('Q')

    #following 3 functions on parsing value taken from the click settings in UI
    def update_click_delay(self, value):
        self.clicker.set_click_delay(value)

    def update_start_delay(self, value):
        self.clicker.set_start_delay(value)

    def update_clicking_method(self, method:str):
        self.clicker.set_click_method(method)

    def update_click_type(self, click_type:str):
        self.clicker.set_click_type(click_type)

    def update_hold_duration(self, duration:int):
        self.clicker.set_hold_duration(duration)

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

    def close_application(self):
        """Close the application when exit key is pressed"""
        print("Exit key pressed, closing application...")
        QApplication.quit()

    def update_cps_display(self, cps):
        """Update the LCD display with current CPS"""
        self.lcdNumber.display(cps)


class ClickerThread(QThread):
    exit_requested = Signal()
    cps_updated = Signal(int)  # Signal to emit CPS updates

    def __init__(self, clicker):
        super().__init__()
        self.clicker = clicker

    def emit_cps(self, cps):
        """Callback function for the clicker to update CPS"""
        self.cps_updated.emit(cps)

    def run(self):
        # Set the CPS callback before starting
        self.clicker.set_cps_callback(self.emit_cps)
        self.clicker.start_clicker()
        # After clicker exits, check if it was due to exit key press
        if self.clicker.exit_requested:
            self.exit_requested.emit()
