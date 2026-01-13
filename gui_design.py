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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QKeySequenceEdit, QLCDNumber, QLabel,
    QLayout, QMainWindow, QSizePolicy, QSlider,
    QSpinBox, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 700)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 680))
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
        self.verticalLayoutWidget_2.setGeometry(QRect(30, 270, 360, 380))
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

        self.clickTypeInput = QComboBox(self.verticalLayoutWidget_2)
        self.clickTypeInput.addItem("")
        self.clickTypeInput.addItem("")
        self.clickTypeInput.addItem("")
        self.clickTypeInput.setObjectName(u"clickTypeInput")

        self.moreSettings.setWidget(0, QFormLayout.ItemRole.FieldRole, self.clickTypeInput)

        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.moreSettings.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.holdDurationSlider = QSlider(self.verticalLayoutWidget_2)
        self.holdDurationSlider.setObjectName(u"holdDurationSlider")
        self.holdDurationSlider.setMinimum(50)
        self.holdDurationSlider.setMaximum(2000)
        self.holdDurationSlider.setValue(500)
        self.holdDurationSlider.setOrientation(Qt.Orientation.Horizontal)

        self.moreSettings.setWidget(1, QFormLayout.ItemRole.FieldRole, self.holdDurationSlider)

        self.label_randomDelay = QLabel(self.verticalLayoutWidget_2)
        self.label_randomDelay.setObjectName(u"label_randomDelay")

        self.moreSettings.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_randomDelay)

        self.randomDelayCheckbox = QCheckBox(self.verticalLayoutWidget_2)
        self.randomDelayCheckbox.setObjectName(u"randomDelayCheckbox")

        self.moreSettings.setWidget(2, QFormLayout.ItemRole.FieldRole, self.randomDelayCheckbox)

        self.label_minDelay = QLabel(self.verticalLayoutWidget_2)
        self.label_minDelay.setObjectName(u"label_minDelay")

        self.moreSettings.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_minDelay)

        self.minDelayInput = QSpinBox(self.verticalLayoutWidget_2)
        self.minDelayInput.setObjectName(u"minDelayInput")
        self.minDelayInput.setMaximum(10000)
        self.minDelayInput.setValue(250)

        self.moreSettings.setWidget(3, QFormLayout.ItemRole.FieldRole, self.minDelayInput)

        self.label_maxDelay = QLabel(self.verticalLayoutWidget_2)
        self.label_maxDelay.setObjectName(u"label_maxDelay")

        self.moreSettings.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_maxDelay)

        self.maxDelayInput = QSpinBox(self.verticalLayoutWidget_2)
        self.maxDelayInput.setObjectName(u"maxDelayInput")
        self.maxDelayInput.setMaximum(10000)
        self.maxDelayInput.setValue(1000)

        self.moreSettings.setWidget(4, QFormLayout.ItemRole.FieldRole, self.maxDelayInput)

        self.label_burstMode = QLabel(self.verticalLayoutWidget_2)
        self.label_burstMode.setObjectName(u"label_burstMode")

        self.moreSettings.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_burstMode)

        self.burstModeCheckbox = QCheckBox(self.verticalLayoutWidget_2)
        self.burstModeCheckbox.setObjectName(u"burstModeCheckbox")

        self.moreSettings.setWidget(5, QFormLayout.ItemRole.FieldRole, self.burstModeCheckbox)

        self.label_burstCount = QLabel(self.verticalLayoutWidget_2)
        self.label_burstCount.setObjectName(u"label_burstCount")

        self.moreSettings.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_burstCount)

        self.burstCountInput = QSpinBox(self.verticalLayoutWidget_2)
        self.burstCountInput.setObjectName(u"burstCountInput")
        self.burstCountInput.setMinimum(1)
        self.burstCountInput.setMaximum(100)
        self.burstCountInput.setValue(5)

        self.moreSettings.setWidget(6, QFormLayout.ItemRole.FieldRole, self.burstCountInput)

        self.label_burstPause = QLabel(self.verticalLayoutWidget_2)
        self.label_burstPause.setObjectName(u"label_burstPause")

        self.moreSettings.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_burstPause)

        self.burstPauseInput = QSpinBox(self.verticalLayoutWidget_2)
        self.burstPauseInput.setObjectName(u"burstPauseInput")
        self.burstPauseInput.setMaximum(10000)
        self.burstPauseInput.setValue(1000)

        self.moreSettings.setWidget(7, QFormLayout.ItemRole.FieldRole, self.burstPauseInput)


        self.moreSettingsContainer.addLayout(self.moreSettings)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(400, 40, 330, 280))
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
        self.startKeyInput.setClearButtonEnabled(True)
        self.startKeyInput.setMaximumSequenceLength(1)

        self.keybindSettings.setWidget(0, QFormLayout.ItemRole.FieldRole, self.startKeyInput)

        self.label_10 = QLabel(self.verticalLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")

        self.keybindSettings.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.stopKeyInput = QKeySequenceEdit(self.verticalLayoutWidget_3)
        self.stopKeyInput.setObjectName(u"stopKeyInput")
        self.stopKeyInput.setClearButtonEnabled(True)
        self.stopKeyInput.setMaximumSequenceLength(1)

        self.keybindSettings.setWidget(1, QFormLayout.ItemRole.FieldRole, self.stopKeyInput)

        self.label_11 = QLabel(self.verticalLayoutWidget_3)
        self.label_11.setObjectName(u"label_11")

        self.keybindSettings.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.exitKeyInput = QKeySequenceEdit(self.verticalLayoutWidget_3)
        self.exitKeyInput.setObjectName(u"exitKeyInput")
        self.exitKeyInput.setClearButtonEnabled(True)
        self.exitKeyInput.setMaximumSequenceLength(1)

        self.keybindSettings.setWidget(2, QFormLayout.ItemRole.FieldRole, self.exitKeyInput)

        self.label_pause = QLabel(self.verticalLayoutWidget_3)
        self.label_pause.setObjectName(u"label_pause")

        self.keybindSettings.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_pause)

        self.pauseKeyInput = QKeySequenceEdit(self.verticalLayoutWidget_3)
        self.pauseKeyInput.setObjectName(u"pauseKeyInput")
        self.pauseKeyInput.setClearButtonEnabled(True)
        self.pauseKeyInput.setMaximumSequenceLength(1)

        self.keybindSettings.setWidget(3, QFormLayout.ItemRole.FieldRole, self.pauseKeyInput)

        self.label_toggle = QLabel(self.verticalLayoutWidget_3)
        self.label_toggle.setObjectName(u"label_toggle")

        self.keybindSettings.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_toggle)

        self.toggleKeyInput = QKeySequenceEdit(self.verticalLayoutWidget_3)
        self.toggleKeyInput.setObjectName(u"toggleKeyInput")
        self.toggleKeyInput.setClearButtonEnabled(True)
        self.toggleKeyInput.setMaximumSequenceLength(1)

        self.keybindSettings.setWidget(4, QFormLayout.ItemRole.FieldRole, self.toggleKeyInput)

        self.label_toggleMode = QLabel(self.verticalLayoutWidget_3)
        self.label_toggleMode.setObjectName(u"label_toggleMode")

        self.keybindSettings.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_toggleMode)

        self.toggleModeCheckbox = QCheckBox(self.verticalLayoutWidget_3)
        self.toggleModeCheckbox.setObjectName(u"toggleModeCheckbox")

        self.keybindSettings.setWidget(5, QFormLayout.ItemRole.FieldRole, self.toggleModeCheckbox)


        self.keybindsContainer.addLayout(self.keybindSettings)

        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(400, 340, 330, 111))
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
        self.line_2.setGeometry(QRect(400, 330, 330, 21))
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
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
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Click Type", None))
        self.clickTypeInput.setItemText(0, QCoreApplication.translate("MainWindow", u"Single Click", None))
        self.clickTypeInput.setItemText(1, QCoreApplication.translate("MainWindow", u"Double Click", None))
        self.clickTypeInput.setItemText(2, QCoreApplication.translate("MainWindow", u"Hold Click", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Hold Duration (ms)", None))
        self.label_randomDelay.setText(QCoreApplication.translate("MainWindow", u"Random Delay", None))
        self.randomDelayCheckbox.setText("")
        self.label_minDelay.setText(QCoreApplication.translate("MainWindow", u"Min Delay (ms)", None))
        self.label_maxDelay.setText(QCoreApplication.translate("MainWindow", u"Max Delay (ms)", None))
        self.label_burstMode.setText(QCoreApplication.translate("MainWindow", u"Burst Mode", None))
        self.burstModeCheckbox.setText("")
        self.label_burstCount.setText(QCoreApplication.translate("MainWindow", u"Burst Click Count", None))
        self.label_burstPause.setText(QCoreApplication.translate("MainWindow", u"Burst Pause (ms)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Start clicking key", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Stop clicking key", None))
        self.stopKeyInput.setKeySequence("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Force close app", None))
        self.label_pause.setText(QCoreApplication.translate("MainWindow", u"Pause/Resume key", None))
        self.label_toggle.setText(QCoreApplication.translate("MainWindow", u"Toggle key (when enabled)", None))
        self.label_toggleMode.setText(QCoreApplication.translate("MainWindow", u"Enable Toggle Mode", None))
        self.toggleModeCheckbox.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CPS", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Clicks per second: ", None))
    # retranslateUi

