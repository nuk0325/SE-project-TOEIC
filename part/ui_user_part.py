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


class Ui_UserPartUI(object):
    def setupUi(self, UserPartUI):
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
        self.frame_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.horizontalLayoutWidget_2 = QWidget(self.frame_3)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 361, 111))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.part1_button = QPushButton(self.frame_8)
        self.part1_button.setObjectName(u"part1_button")
        self.part1_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.part1_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")
        self.label = QtWidgets.QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(35, 70, 101, 20))
        self.label.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_2.addWidget(self.frame_8)

        self.frame_7 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.part2_button = QPushButton(self.frame_7)
        self.part2_button.setObjectName(u"part2_button")
        self.part2_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.part2_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(35, 70, 101, 20))
        self.label_2.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_2.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_6 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.horizontalLayoutWidget_3 = QWidget(self.frame_6)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 361, 111))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QtWidgets.QFrame(self.horizontalLayoutWidget_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.part3_button = QPushButton(self.frame_9)
        self.part3_button.setObjectName(u"part3_button")
        self.part3_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.part3_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")
        self.label_3 = QtWidgets.QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(35, 70, 101, 20))
        self.label_3.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QtWidgets.QFrame(self.horizontalLayoutWidget_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.part4_button = QPushButton(self.frame_10)
        self.part4_button.setObjectName(u"part4_button")
        self.part4_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.part4_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")
        self.label_4 = QtWidgets.QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(35, 70, 101, 20))
        self.label_4.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_3.addWidget(self.frame_10)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_5 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.horizontalLayoutWidget_4 = QWidget(self.frame_5)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 361, 111))
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QtWidgets.QFrame(self.horizontalLayoutWidget_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.part5_button = QPushButton(self.frame_11)
        self.part5_button.setObjectName(u"part5_button")
        self.part5_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.part5_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")
        self.label_5 = QtWidgets.QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(35, 70, 101, 20))
        self.label_5.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_4.addWidget(self.frame_11)

        self.frame_12 = QtWidgets.QFrame(self.horizontalLayoutWidget_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.part6_button = QPushButton(self.frame_12)
        self.part6_button.setObjectName(u"part6_button")
        self.part6_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.part6_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")
        self.label_6 = QtWidgets.QLabel(self.frame_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(35, 70, 101, 20))
        self.label_6.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_4.addWidget(self.frame_12)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_4 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.horizontalLayoutWidget_5 = QWidget(self.frame_4)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 361, 111))
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QtWidgets.QFrame(self.horizontalLayoutWidget_5)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.part7_button = QPushButton(self.frame_14)
        self.part7_button.setObjectName(u"part7_button")
        self.part7_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.part7_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")
        self.label_7 = QtWidgets.QLabel(self.frame_14)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(35, 70, 101, 20))
        self.label_7.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_5.addWidget(self.frame_14)

        self.frame_13 = QtWidgets.QFrame(self.horizontalLayoutWidget_5)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.part8_button = QPushButton(self.frame_13)
        self.part8_button.setObjectName(u"part8_button")
        self.part8_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.part8_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")
        self.label_8 = QtWidgets.QLabel(self.frame_13)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(True)
        self.label_8.setGeometry(QtCore.QRect(35, 70, 101, 20))
        self.label_8.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_5.addWidget(self.frame_13)


        self.verticalLayout.addWidget(self.frame_4)

        UserPartUI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UserPartUI)
        self.statusbar.setObjectName(u"statusbar")
        UserPartUI.setStatusBar(self.statusbar)

        self.back_button.clicked.connect(self.back_button_clicked)#뒤로가기
        self.home_button.clicked.connect(self.home_button_clicked)#홈
        self.part1_button.clicked.connect(self.part1_button_clicked)#Part1 ~ Part8
        self.part2_button.clicked.connect(self.part2_button_clicked)
        self.part3_button.clicked.connect(self.part3_button_clicked)
        self.part4_button.clicked.connect(self.part4_button_clicked)
        self.part5_button.clicked.connect(self.part5_button_clicked)
        self.part6_button.clicked.connect(self.part6_button_clicked)
        self.part7_button.clicked.connect(self.part7_button_clicked)
        self.part8_button.clicked.connect(self.part8_button_clicked)

        self.retranslateUi(UserPartUI)

        QtCore.QMetaObject.connectSlotsByName(UserPartUI)
    
    #버튼 이벤트
    def back_button_clicked(self):
        print(f"뒤로가기를 눌렀습니다.")
        
    def home_button_clicked(self):
        print(f"홈버튼을 눌렀습니다.")
    
    def part1_button_clicked(self):
        print(f"Part 1이 선택되었습니다.")

    def part2_button_clicked(self):
        print(f"Part 2이 선택되었습니다.")

    def part3_button_clicked(self):
        print(f"Part 3이 선택되었습니다.")

    def part4_button_clicked(self):
        print(f"Part 4이 선택되었습니다.")

    def part5_button_clicked(self):
        print(f"Part 5이 선택되었습니다.")

    def part6_button_clicked(self):
        print(f"Part 6이 선택되었습니다.")

    def part7_button_clicked(self):
        print(f"Part 7이 선택되었습니다.")

    def part8_button_clicked(self):
        print(f"Part 8이 선택되었습니다.")
    
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
        self.part1_button.setText(QtCore.QCoreApplication.translate("UserPartUI", u"Part 1", None))
        self.label.setText(QtCore.QCoreApplication.translate("UserPartUI", u"userStudiedNum", None))
        self.part2_button.setText(QtCore.QCoreApplication.translate("UserPartUI", u"Part 2", None))
        self.label_2.setText(QtCore.QCoreApplication.translate("UserPartUI", u"userStudiedNum", None))
        self.part3_button.setText(QtCore.QCoreApplication.translate("UserPartUI", u"Part 3", None))
        self.label_3.setText(QtCore.QCoreApplication.translate("UserPartUI", u"userStudiedNum", None))
        self.part4_button.setText(QtCore.QCoreApplication.translate("UserPartUI", u"Part 4", None))
        self.label_4.setText(QtCore.QCoreApplication.translate("UserPartUI", u"userStudiedNum", None))
        self.part5_button.setText(QtCore.QCoreApplication.translate("UserPartUI", u"Part 5", None))
        self.label_5.setText(QtCore.QCoreApplication.translate("UserPartUI", u"userStudiedNum", None))
        self.part6_button.setText(QtCore.QCoreApplication.translate("UserPartUI", u"Part 6", None))
        self.label_6.setText(QtCore.QCoreApplication.translate("UserPartUI", u"userStudiedNum", None))
        self.part7_button.setText(QtCore.QCoreApplication.translate("UserPartUI", u"Part 7", None))
        self.label_7.setText(QtCore.QCoreApplication.translate("UserPartUI", u"userStudiedNum", None))
        self.part8_button.setText(QtCore.QCoreApplication.translate("UserPartUI", u"Part 8", None))
        self.label_8.setText(QtCore.QCoreApplication.translate("UserPartUI", u"userStudiedNum", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserpartUI = QtWidgets.QMainWindow()
    ui = Ui_UserPartUI()
    ui.setupUi(UserpartUI)
    UserpartUI.show()
    sys.exit(app.exec())