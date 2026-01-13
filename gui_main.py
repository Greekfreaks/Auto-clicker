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

        # Connect advanced timing widgets
        self.randomDelayCheckbox.stateChanged.connect(self.update_random_delay)
        self.minDelayInput.valueChanged.connect(self.update_min_delay)
        self.maxDelayInput.valueChanged.connect(self.update_max_delay)
        self.burstModeCheckbox.stateChanged.connect(self.update_burst_mode)
        self.burstCountInput.valueChanged.connect(self.update_burst_count)
        self.burstPauseInput.valueChanged.connect(self.update_burst_pause)

        #read the inputted keybinds
        self.startKeyInput.keySequenceChanged.connect(self.update_start_key)
        self.startKeyInput.setKeySequence('S')
        self.stopKeyInput.keySequenceChanged.connect(self.update_stop_key)
        self.stopKeyInput.setKeySequence('X')
        self.exitKeyInput.keySequenceChanged.connect(self.update_exit_key)
        self.exitKeyInput.setKeySequence('Q')
        self.pauseKeyInput.keySequenceChanged.connect(self.update_pause_key)
        self.pauseKeyInput.setKeySequence('P')
        self.toggleKeyInput.keySequenceChanged.connect(self.update_toggle_key)
        self.toggleKeyInput.setKeySequence('T')

        # Connect toggle mode checkbox
        self.toggleModeCheckbox.stateChanged.connect(self.update_toggle_mode)

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

    def update_pause_key(self, sequence):
        keystrokes = sequence.toString().lower()
        self.clicker.set_pause_key(keystrokes)

    def update_toggle_key(self, sequence):
        keystrokes = sequence.toString().lower()
        self.clicker.set_toggle_key(keystrokes)

    def update_toggle_mode(self, state):
        self.clicker.set_toggle_mode(state == 2)  # 2 = Qt.Checked

    def update_random_delay(self, state):
        self.clicker.set_random_delay(state == 2)

    def update_min_delay(self, value):
        self.clicker.set_min_delay(value)

    def update_max_delay(self, value):
        self.clicker.set_max_delay(value)

    def update_burst_mode(self, state):
        self.clicker.set_burst_mode(state == 2)

    def update_burst_count(self, value):
        self.clicker.set_burst_count(value)

    def update_burst_pause(self, value):
        self.clicker.set_burst_pause(value)

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
