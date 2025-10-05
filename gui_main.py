from PyQt6.QtWidgets import QApplication, QMainWindow
from gui_design import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app = QApplication(sys.argv)
window = MainWindow()
window.show()  
app.exec()