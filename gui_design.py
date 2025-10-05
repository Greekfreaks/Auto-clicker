# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_design.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QFormLayout, QFrame, QKeySequenceEdit, QLCDNumber,
    QLabel, QLayout, QMainWindow, QSizePolicy,
    QSlider, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(645, 485)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(644, 450))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 311, 221))
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

        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 0))
        self.comboBox.setMaximumSize(QSize(16777215, 16777215))

        self.autoClickSettings.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBox)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.autoClickSettings.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.autoClickSettings.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.doubleSpinBox = QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMaximum(10000.000000000000000)

        self.autoClickSettings.setWidget(1, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setReadOnly(False)
        self.doubleSpinBox_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.doubleSpinBox_2.setDecimals(1)
        self.doubleSpinBox_2.setMaximum(10000.000000000000000)

        self.autoClickSettings.setWidget(2, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_2)


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

        self.keySequenceEdit = QKeySequenceEdit(self.verticalLayoutWidget_3)
        self.keySequenceEdit.setObjectName(u"keySequenceEdit")

        self.keybindSettings.setWidget(0, QFormLayout.ItemRole.FieldRole, self.keySequenceEdit)

        self.label_10 = QLabel(self.verticalLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")

        self.keybindSettings.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.keySequenceEdit_2 = QKeySequenceEdit(self.verticalLayoutWidget_3)
        self.keySequenceEdit_2.setObjectName(u"keySequenceEdit_2")

        self.keybindSettings.setWidget(1, QFormLayout.ItemRole.FieldRole, self.keySequenceEdit_2)

        self.label_11 = QLabel(self.verticalLayoutWidget_3)
        self.label_11.setObjectName(u"label_11")

        self.keybindSettings.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.keySequenceEdit_3 = QKeySequenceEdit(self.verticalLayoutWidget_3)
        self.keySequenceEdit_3.setObjectName(u"keySequenceEdit_3")

        self.keybindSettings.setWidget(2, QFormLayout.ItemRole.FieldRole, self.keySequenceEdit_3)


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
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Left Click", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Right Click", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Middle Click", None))

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
    # retranslateUi

