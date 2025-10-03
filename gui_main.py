import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt

app = QApplication([])
window = QMainWindow()

#set-up window application
window.setMinimumSize(700, 460)
window.setWindowTitle('Auto Clicker')
window.setWindowIcon(QIcon('mouse_icon.jpg'))

#add widgets
label = QLabel("Test text", alignment=Qt.AlignmentFlag.AlignCenter )
font = window.font()
font.setPointSize(12)
font.setBold(True)
label.setFont(font)
window.setCentralWidget(label)

#image widget
image = QLabel()
image.setPixmap(QPixmap('mouse_icon.jpg').scaled(56, 56))
window.setCentralWidget(image)

#button widget
button = QPushButton("button")
window.setCentralWidget(button)

#show and run window
window.show()
app.exec()