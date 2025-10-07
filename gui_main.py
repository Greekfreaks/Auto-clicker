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

        self.clickDelayInput.valueChanged.connect(self.update_click_delay)

    def update_click_delay(self, value):
        print(f"Delay set to {value}")
        self.clicker.set_click_delay(value)

class ClickerThread(QThread):
    def __init__(self, clicker):
        super().__init__()
        self.clicker = clicker

    def run(self):
        self.clicker.start_clicker()





