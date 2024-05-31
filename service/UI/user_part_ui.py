# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_partabgeSB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QPushButton, QApplication, QWidget


class UserPartUI(object):
    def setupUi(self, UserPartUI, unitNumberList):
        self.parent = UserPartUI

        if not UserPartUI.objectName():
            UserPartUI.setObjectName(u"UserPartUI")

        UserPartUI.resize(360, 600)
        UserPartUI.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.centralwidget = QWidget(UserPartUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 360, 60))
        self.frame_2.setStyleSheet(u"background-color: rgba(253, 213, 51, 0.97)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.horizontalLayoutWidget = QWidget(self.frame_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 361, 89))
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

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QtCore.QRect(0, 60, 360, 511))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 361, 511))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        
        # List to hold button and label references
        self.buttons = []
        self.labels = []

        for i in range(4):
            frame = QtWidgets.QFrame(self.verticalLayoutWidget)
            frame.setObjectName(f"frame_{i + 3}")
            frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
            horizontalLayoutWidget = QWidget(frame)
            horizontalLayoutWidget.setObjectName(f"horizontalLayoutWidget_{i + 2}")
            horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 361, 111))
            horizontalLayout = QtWidgets.QHBoxLayout(horizontalLayoutWidget)
            horizontalLayout.setObjectName(f"horizontalLayout_{i + 2}")
            horizontalLayout.setContentsMargins(0, 0, 0, 0)

            for j in range(2):
                part_frame = QtWidgets.QFrame(horizontalLayoutWidget)
                part_frame.setObjectName(f"frame_{i * 2 + j + 8}")
                part_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)

                part_button = QPushButton(part_frame)
                part_button.setObjectName(f"part{i * 2 + j + 1}_button")
                part_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
                part_button.setText(f"Part {i * 2 + j + 1}")

                if unitNumberList[i * 2 + j] == 0:
                    part_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")
                elif unitNumberList[i * 2 + j] < 15:
                    part_button.setStyleSheet(u"background-color: rgba(250, 220, 104, 0.7)")
                else:
                    part_button.setStyleSheet(u"background-color: rgba(36, 174, 95, 0.8)")
                
                part_unit_num = QtWidgets.QLabel(part_frame)
                part_unit_num.setObjectName(f"part{i * 2 + j + 1}_unit_num")
                part_unit_num.setEnabled(True)
                part_unit_num.setGeometry(QtCore.QRect(35, 70, 101, 20))
                part_unit_num.setText(f"         {unitNumberList[i * 2 + j]} / 15")
                part_unit_num.setStyleSheet(u"background-color: transparent")

                # Add to list for later access
                self.buttons.append(part_button)
                self.labels.append(part_unit_num)

                part_button.clicked.connect(lambda _, b=part_button: self.partButtonClicked(b))

                horizontalLayout.addWidget(part_frame)

            self.verticalLayout.addWidget(frame)

        UserPartUI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UserPartUI)
        self.statusbar.setObjectName(u"statusbar")
        UserPartUI.setStatusBar(self.statusbar)

        self.retranslateUi(UserPartUI)

        QtCore.QMetaObject.connectSlotsByName(UserPartUI)
    
    # setupUi
    def retranslateUi(self, UserPartUI):
        UserPartUI.setWindowTitle(QtCore.QCoreApplication.translate("UserPartUI", u"MainWindow", None))
        self.back_button.setText(QtCore.QCoreApplication.translate("UserPartUI", u"\ub4a4\ub85c\uac00\uae30", None))
        self.menu_name.setHtml(QtCore.QCoreApplication.translate("UserPartUI", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:'Gulim'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont'; font-size:20pt; font-weight:696;\">\ud559\uc2b5\ud558\uae30</span></p></body></html>", None))
        self.home_button.setText(QtCore.QCoreApplication.translate("UserPartUI", u"\ud648", None))


    def partButtonClicked(self, button):
        # print(f"{button.text()}이 선택되었습니다.")
        
        if button.text() == "Part 1":
            self.parent.part1_button_clicked()
        elif button.text() == "Part 2":
            self.parent.part2_button_clicked()
        elif button.text() == "Part 3":
            self.parent.part3_button_clicked()
        elif button.text() == "Part 4":
            self.parent.part4_button_clicked()
        elif button.text() == "Part 5":
            self.parent.part5_button_clicked()
        elif button.text() == "Part 6":
            self.parent.part6_button_clicked()
        elif button.text() == "Part 7":
            self.parent.Part7_button_clicked()
        elif button.text() == "Part 8":
            self.parent.Part8_button_clicked()
        else:
            print("잘못된 버튼 클릭") 


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     UserpartUI = QtWidgets.QMainWindow()
#     ui = UserPartUI()
#     ui.setupUi(UserpartUI, [1, 2, 3, 4, 5, 6, 7, 8])
#     UserpartUI.show()
#     sys.exit(app.exec())
