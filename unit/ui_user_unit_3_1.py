# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_unit_2PkJpPq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QPushButton, QApplication, QWidget, QScrollArea


class Ui_UserUnitUI(object):
    def setupUi(self, UserUnitUI):
        if not UserUnitUI.objectName():
            UserUnitUI.setObjectName(u"UserUnitUI")
        UserUnitUI.resize(360, 600)
        UserUnitUI.setMinimumSize(QtCore.QSize(360, 600))
        UserUnitUI.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.centralwidget = QWidget(UserUnitUI)
        self.centralwidget.setObjectName(u"centralwidget")

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QtCore.QRect(0, 60, 360, 540))
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 360, 1200))
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 360, 60))
        self.frame_2.setStyleSheet(u"background-color: rgba(253, 213, 51, 0.97)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.horizontalLayoutWidget = QWidget(self.frame_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 383, 89))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.back_button = QPushButton(self.horizontalLayoutWidget)
        self.back_button.setObjectName(u"back_button")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.back_button)

        self.menu_name = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.menu_name.setObjectName(u"menu_name")
        sizePolicy1 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menu_name.sizePolicy().hasHeightForWidth())
        self.menu_name.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.menu_name)

        self.home_button = QPushButton(self.horizontalLayoutWidget)
        self.home_button.setObjectName(u"home_button")
        sizePolicy.setHeightForWidth(self.home_button.sizePolicy().hasHeightForWidth())
        self.home_button.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.home_button)

        # Add buttons to scroll area
        for i in range(1, 16, 2):
            frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            frame.setObjectName(f"frame_{i}")
            frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            frame_layout = QtWidgets.QHBoxLayout(frame)
            frame_layout.setObjectName(f"horizontalLayout_{i}")

            button1 = QPushButton(frame)
            button1.setObjectName(f"unit{i}_button")
            button1.setFixedSize(150, 120)  # Set button size
            button1.setStyleSheet(u"background-color: rgb(190, 190, 190)")
            button1.setText(f"Unit {i}")

            frame_layout.addWidget(button1)
            button1.clicked.connect(lambda _, b=button1: self.unit_button_clicked(b))

            if i + 1 <= 15:
                button2 = QPushButton(frame)
                button2.setObjectName(f"unit{i+1}_button")
                button2.setFixedSize(150, 120)  # Set button size
                button2.setStyleSheet(u"background-color: rgb(190, 190, 190)")
                button2.setText(f"Unit {i+1}")

                frame_layout.addWidget(button2)
                button2.clicked.connect(lambda _, b=button2: self.unit_button_clicked(b))

            self.verticalLayout.addWidget(frame)

        UserUnitUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserUnitUI)
        QtCore.QMetaObject.connectSlotsByName(UserUnitUI)

        self.back_button.clicked.connect(self.back_button_clicked) #뒤로가기
        self.home_button.clicked.connect(self.home_button_clicked) #홈

    def unit_button_clicked(self, button):
        print(f"{button.text()}이 선택되었습니다.")

    def back_button_clicked(self):
        print(f"뒤로가기를 눌렀습니다.")
        
    def home_button_clicked(self):
        print(f"홈버튼을 눌렀습니다.")

    def retranslateUi(self, UserUnitUI):
        UserUnitUI.setWindowTitle(QtCore.QCoreApplication.translate("UserUnitUI", u"MainWindow", None))
        self.back_button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"뒤로가기", None))
        self.menu_name.setHtml(QtCore.QCoreApplication.translate("UserUnitUI", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Gulim'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont'; font-size:20pt; font-weight:696;\">Part1</span></p></body></html>", None))
        self.home_button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"홈", None))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    UserUnitUI = QtWidgets.QMainWindow()
    ui = Ui_UserUnitUI()
    ui.setupUi(UserUnitUI)
    UserUnitUI.show()
    sys.exit(app.exec())
