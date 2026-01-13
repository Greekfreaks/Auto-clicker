from gui_main import MainWindow, ClickerThread
from PySide6.QtWidgets import QApplication


app = QApplication()
window = MainWindow()
window.show()
app.exec()