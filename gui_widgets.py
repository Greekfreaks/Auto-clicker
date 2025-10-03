from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto Clicker")
        self.setWindowIcon(QIcon('mouse_icon.jpg'))
        self.setMinimumSize(700, 460)
        self.setStyleSheet('background-color:#fff')


app = QApplication([])
window = Window()

window.show()
app.exec()