# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGroupBox, QKeySequenceEdit, QLCDNumber, QLabel,
    QLayout, QMainWindow, QSizePolicy, QSlider,
    QSpinBox, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(869, 660)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(644, 450))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 311, 231))
        self.autoClickContainer = QVBoxLayout(self.verticalLayoutWidget)
        self.autoClickContainer.setSpacing(0)
        self.autoClickContainer.setObjectName(u"autoClickContainer")
        self.autoClickContainer.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.autoClickContainer.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_4.setFont(font)

        self.autoClickContainer.addWidget(self.label_4)

        self.autoClickSettings = QFormLayout()
        self.autoClickSettings.setObjectName(u"autoClickSettings")
        self.autoClickSettings.setHorizontalSpacing(25)
        self.autoClickSettings.setVerticalSpacing(35)
        self.autoClickSettings.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.autoClickSettings.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.clickingMethodInput = QComboBox(self.verticalLayoutWidget)
        self.clickingMethodInput.addItem("")
        self.clickingMethodInput.addItem("")
        self.clickingMethodInput.addItem("")
        self.clickingMethodInput.setObjectName(u"clickingMethodInput")
        self.clickingMethodInput.setMinimumSize(QSize(0, 0))
        self.clickingMethodInput.setMaximumSize(QSize(16777215, 16777215))

        self.autoClickSettings.setWidget(0, QFormLayout.ItemRole.FieldRole, self.clickingMethodInput)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.autoClickSettings.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.autoClickSettings.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.clickDelayInput = QSpinBox(self.verticalLayoutWidget)
        self.clickDelayInput.setObjectName(u"clickDelayInput")
        self.clickDelayInput.setMaximum(10000)
        self.clickDelayInput.setValue(250)

        self.autoClickSettings.setWidget(1, QFormLayout.ItemRole.FieldRole, self.clickDelayInput)

        self.startDelayInput = QSpinBox(self.verticalLayoutWidget)
        self.startDelayInput.setObjectName(u"startDelayInput")
        self.startDelayInput.setMaximum(10000)
        self.startDelayInput.setValue(50)

        self.autoClickSettings.setWidget(2, QFormLayout.ItemRole.FieldRole, self.startDelayInput)


        self.autoClickContainer.addLayout(self.autoClickSettings)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(30, 270, 311, 151))
        self.moreSettingsContainer = QVBoxLayout(self.verticalLayoutWidget_2)
        self.moreSettingsContainer.setObjectName(u"moreSettingsContainer")
        self.moreSettingsContainer.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.moreSettingsContainer.addWidget(self.label_7)

        self.moreSettings = QFormLayout()
        self.moreSettings.setObjectName(u"moreSettings")
        self.moreSettings.setHorizontalSpacing(25)
        self.moreSettings.setVerticalSpacing(35)
        self.moreSettings.setContentsMargins(10, 10, 10, 10)
        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.moreSettings.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.comboBox_2 = QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.moreSettings.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBox_2)

        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.moreSettings.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.horizontalSlider_3 = QSlider(self.verticalLayoutWidget_2)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setOrientation(Qt.Orientation.Horizontal)

        self.moreSettings.setWidget(1, QFormLayout.ItemRole.FieldRole, self.horizontalSlider_3)


        self.moreSettingsContainer.addLayout(self.moreSettings)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(400, 40, 211, 171))
        self.keybindsContainer = QVBoxLayout(self.verticalLayoutWidget_3)
        self.keybindsContainer.setObjectName(u"keybindsContainer")
        self.keybindsContainer.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.verticalLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_8.setFont(font1)

        self.keybindsContainer.addWidget(self.label_8)

        self.keybindSettings = QFormLayout()
        self.keybindSettings.setObjectName(u"keybindSettings")
        self.keybindSettings.setHorizontalSpacing(20)
        self.keybindSettings.setVerticalSpacing(25)
        self.label_9 = QLabel(self.verticalLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")

        self.keybindSettings.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.startKeyInput = QKeySequenceEdit(self.verticalLayoutWidget_3)
        self.startKeyInput.setObjectName(u"startKeyInput")

        self.keybindSettings.setWidget(0, QFormLayout.ItemRole.FieldRole, self.startKeyInput)

        self.label_10 = QLabel(self.verticalLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")

        self.keybindSettings.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.stopKeyInput = QKeySequenceEdit(self.verticalLayoutWidget_3)
        self.stopKeyInput.setObjectName(u"stopKeyInput")

        self.keybindSettings.setWidget(1, QFormLayout.ItemRole.FieldRole, self.stopKeyInput)

        self.label_11 = QLabel(self.verticalLayoutWidget_3)
        self.label_11.setObjectName(u"label_11")

        self.keybindSettings.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.exitKeyInput = QKeySequenceEdit(self.verticalLayoutWidget_3)
        self.exitKeyInput.setObjectName(u"exitKeyInput")

        self.keybindSettings.setWidget(2, QFormLayout.ItemRole.FieldRole, self.exitKeyInput)


        self.keybindsContainer.addLayout(self.keybindSettings)

        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(400, 240, 211, 111))
        self.CPSContainer = QVBoxLayout(self.verticalLayoutWidget_4)
        self.CPSContainer.setObjectName(u"CPSContainer")
        self.CPSContainer.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.verticalLayoutWidget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.CPSContainer.addWidget(self.label_12)

        self.CPSSettings = QFormLayout()
        self.CPSSettings.setObjectName(u"CPSSettings")
        self.CPSSettings.setHorizontalSpacing(20)
        self.CPSSettings.setVerticalSpacing(25)
        self.label_13 = QLabel(self.verticalLayoutWidget_4)
        self.label_13.setObjectName(u"label_13")

        self.CPSSettings.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_13)

        self.lcdNumber = QLCDNumber(self.verticalLayoutWidget_4)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setSmallDecimalPoint(False)

        self.CPSSettings.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lcdNumber)


        self.CPSContainer.addLayout(self.CPSSettings)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(30, 260, 311, 21))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(400, 230, 211, 21))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 430, 311, 131))
        self.groupBox.setStyleSheet(u"background-color: rgb(180, 180, 180);\n"
"color: rgb(0, 0, 0);")
        self.layoutWidget = QWidget(self.groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 291, 101))
        self.moreSettings_2 = QFormLayout(self.layoutWidget)
        self.moreSettings_2.setObjectName(u"moreSettings_2")
        self.moreSettings_2.setHorizontalSpacing(25)
        self.moreSettings_2.setVerticalSpacing(35)
        self.moreSettings_2.setContentsMargins(10, 10, 10, 10)
        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.moreSettings_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_14)

        self.comboBox_3 = QComboBox(self.layoutWidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.moreSettings_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBox_3)

        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.moreSettings_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_15)

        self.horizontalSlider_4 = QSlider(self.layoutWidget)
        self.horizontalSlider_4.setObjectName(u"horizontalSlider_4")
        self.horizontalSlider_4.setOrientation(Qt.Orientation.Horizontal)

        self.moreSettings_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.horizontalSlider_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Auto Clicker", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Auto clicking settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Method of clicking", None))
        self.clickingMethodInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Left Click", None))
        self.clickingMethodInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Right Click", None))
        self.clickingMethodInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Middle Click", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Delay between clicks (ms)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Delay before clicking (ms)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"More Settings", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Setting 1", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Left Click", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Right Click", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Middle Click", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Setting 2", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Start clicking key", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Stop clicking key", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Force close app", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CPS", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Clicks per second: ", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"More Settings", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Setting 1", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Left Click", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Right Click", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Middle Click", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Setting 2", None))
    # retranslateUi

