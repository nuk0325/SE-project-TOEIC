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

        self.frame_1 = QtWidgets.QFrame(self.scrollArea)
        self.frame_1.setObjectName(u"frame")
        self.frame_1.setGeometry(QtCore.QRect(0, 0, 360, 1200))
        self.frame_1.setMinimumSize(QtCore.QSize(360, 540))
        self.frame_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.verticalLayoutWidget = QWidget(self.frame_1)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 361, 1201))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_50 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        #self.frame_50.setFrameShadow(QtWidgets.QFrame.raise_)
        self.horizontalLayoutWidget_22 = QWidget(self.frame_50)
        self.horizontalLayoutWidget_22.setObjectName(u"horizontalLayoutWidget_22")
        self.horizontalLayoutWidget_22.setGeometry(QtCore.QRect(0, 0, 361, 111))
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_22)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_51 = QtWidgets.QFrame(self.horizontalLayoutWidget_22)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        #self.frame_51.setFrameShadow(QtWidgets.QFrame.raise_)
        self.unit1_button = QPushButton(self.frame_51)
        self.unit1_button.setObjectName(u"unit1_button")
        self.unit1_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.unit1_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_23.addWidget(self.frame_51)

        self.frame_52 = QtWidgets.QFrame(self.horizontalLayoutWidget_22)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_52.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        #self.frame_52.setFrameShadow(QtWidgets.QFrame.raise_)
        self.unit2_button = QPushButton(self.frame_52)
        self.unit2_button.setObjectName(u"unit2_button")
        self.unit2_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.unit2_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_23.addWidget(self.frame_52)


        self.verticalLayout.addWidget(self.frame_50)

        self.frame_47 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        #self.frame_47.setFrameShadow(QtWidgets.QFrame.raise_)
        self.horizontalLayoutWidget_21 = QWidget(self.frame_47)
        self.horizontalLayoutWidget_21.setObjectName(u"horizontalLayoutWidget_21")
        self.horizontalLayoutWidget_21.setGeometry(QtCore.QRect(0, 0, 361, 111))
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_21)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_48 = QtWidgets.QFrame(self.horizontalLayoutWidget_21)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        #self.frame_48.setFrameShadow(QtWidgets.QFrame.raise_)
        self.unit3_button = QPushButton(self.frame_48)
        self.unit3_button.setObjectName(u"unit3_button")
        self.unit3_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.unit3_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_22.addWidget(self.frame_48)

        self.frame_49 = QtWidgets.QFrame(self.horizontalLayoutWidget_21)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_49.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        #self.frame_49.setFrameShadow(QtWidgets.QFrame.raise_)
        self.unit4_button = QPushButton(self.frame_49)
        self.unit4_button.setObjectName(u"unit4_button")
        self.unit4_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.unit4_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_22.addWidget(self.frame_49)


        self.verticalLayout.addWidget(self.frame_47)

        self.frame_42 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        #self.frame_42.setFrameShadow(QtWidgets.QFrame.raise_)
        self.horizontalLayoutWidget_20 = QWidget(self.frame_42)
        self.horizontalLayoutWidget_20.setObjectName(u"horizontalLayoutWidget_20")
        self.horizontalLayoutWidget_20.setGeometry(QtCore.QRect(0, 0, 361, 111))
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_45 = QtWidgets.QFrame(self.horizontalLayoutWidget_20)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        #self.frame_45.setFrameShadow(QtWidgets.QFrame.raise_)
        self.unit5_button = QPushButton(self.frame_45)
        self.unit5_button.setObjectName(u"unit5_button")
        self.unit5_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.unit5_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_21.addWidget(self.frame_45)

        self.frame_46 = QtWidgets.QFrame(self.horizontalLayoutWidget_20)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_46.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        #self.frame_46.setFrameShadow(QtWidgets.QFrame.raise_)
        self.unit6_button = QPushButton(self.frame_46)
        self.unit6_button.setObjectName(u"unit6_button")
        self.unit6_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.unit6_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_21.addWidget(self.frame_46)


        self.verticalLayout.addWidget(self.frame_42)

        self.frame_15 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        #self.frame_15.setFrameShadow(QtWidgets.QFrame.raise_)
        self.horizontalLayoutWidget_18 = QWidget(self.frame_15)
        self.horizontalLayoutWidget_18.setObjectName(u"horizontalLayoutWidget_18")
        self.horizontalLayoutWidget_18.setGeometry(QtCore.QRect(0, 0, 361, 111))
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_18)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_41 = QtWidgets.QFrame(self.horizontalLayoutWidget_18)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        #self.frame_41.setFrameShadow(QtWidgets.QFrame.raise_)
        self.unit7_button = QPushButton(self.frame_41)
        self.unit7_button.setObjectName(u"unit7_button")
        self.unit7_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.unit7_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_19.addWidget(self.frame_41)

        self.frame_28 = QtWidgets.QFrame(self.horizontalLayoutWidget_18)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_28.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        #self.frame_28.setFrameShadow(QtWidgets.QFrame.raise_)
        self.unit8_button = QPushButton(self.frame_28)
        self.unit8_button.setObjectName(u"unit8_button")
        self.unit8_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.unit8_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_19.addWidget(self.frame_28)


        self.verticalLayout.addWidget(self.frame_15)

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
        self.unit9_button = QPushButton(self.frame_8)
        self.unit9_button.setObjectName(u"unit9_button")
        self.unit9_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.unit9_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_2.addWidget(self.frame_8)

        self.frame_7 = QtWidgets.QFrame(self.horizontalLayoutWidget_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.unit10_button = QPushButton(self.frame_7)
        self.unit10_button.setObjectName(u"unit10_button")
        self.unit10_button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.unit10_button.setStyleSheet(u"background-color: rgb(190, 190, 190)")

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
        self.unit11_Button = QPushButton(self.frame_9)
        self.unit11_Button.setObjectName(u"unit11_Button")
        self.unit11_Button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.unit11_Button.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QtWidgets.QFrame(self.horizontalLayoutWidget_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.unit12_Button = QPushButton(self.frame_10)
        self.unit12_Button.setObjectName(u"unit12_Button")
        self.unit12_Button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.unit12_Button.setStyleSheet(u"background-color: rgb(190, 190, 190)")

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
        self.unit13_Button = QPushButton(self.frame_11)
        self.unit13_Button.setObjectName(u"unit13_Button")
        self.unit13_Button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.unit13_Button.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_4.addWidget(self.frame_11)

        self.frame_12 = QtWidgets.QFrame(self.horizontalLayoutWidget_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.unit14_Button = QPushButton(self.frame_12)
        self.unit14_Button.setObjectName(u"unit14_Button")
        self.unit14_Button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.unit14_Button.setStyleSheet(u"background-color: rgb(190, 190, 190)")

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
        self.unit15_Button = QPushButton(self.frame_14)
        self.unit15_Button.setObjectName(u"unit15_Button")
        self.unit15_Button.setGeometry(QtCore.QRect(10, 10, 150, 90))
        self.unit15_Button.setStyleSheet(u"background-color: rgb(190, 190, 190)")

        self.horizontalLayout_5.addWidget(self.frame_14)


        self.verticalLayout.addWidget(self.frame_4)

        #self.frame_15.raise_()
        #self.frame_3.raise_()
        #self.frame_6.raise_()
        #self.frame_5.raise_()
        #self.frame_4.raise_()
        #self.frame_42.raise_()
        #self.frame_47.raise_()
        #self.frame_50.raise_()
       
        self.back_button.clicked.connect(self.back_button_clicked)#뒤로가기
        self.home_button.clicked.connect(self.home_button_clicked)#홈
        self.unit1_button.clicked.connect(self.unit1_button_clicked)#Unit1 ~ Unit15
        self.unit2_button.clicked.connect(self.unit2_button_clicked)
        self.unit3_button.clicked.connect(self.unit3_button_clicked)
        self.unit4_button.clicked.connect(self.unit4_button_clicked)
        self.unit5_button.clicked.connect(self.unit5_button_clicked)
        self.unit6_button.clicked.connect(self.unit6_button_clicked)
        self.unit7_button.clicked.connect(self.unit7_button_clicked)
        self.unit8_button.clicked.connect(self.unit8_button_clicked)
        self.unit9_button.clicked.connect(self.unit9_button_clicked)
        self.unit10_button.clicked.connect(self.unit10_button_clicked)
        self.unit11_Button.clicked.connect(self.unit11_button_clicked)
        self.unit12_Button.clicked.connect(self.unit12_button_clicked)
        self.unit13_Button.clicked.connect(self.unit13_button_clicked)
        self.unit14_Button.clicked.connect(self.unit14_button_clicked)
        self.unit15_Button.clicked.connect(self.unit15_button_clicked)
        

        UserUnitUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserUnitUI)
        self.scrollArea.setWidget(self.frame_1)

        QtCore.QMetaObject.connectSlotsByName(UserUnitUI)

    #버튼 이벤트
    def back_button_clicked(self):
        print(f"뒤로가기를 눌렀습니다.")
        
    def home_button_clicked(self):
        print(f"홈버튼을 눌렀습니다.")
    
    def unit1_button_clicked(self):
        print(f"Unit 1이 선택되었습니다.")

    def unit2_button_clicked(self):
        print(f"Unit 2이 선택되었습니다.")

    def unit3_button_clicked(self):
        print(f"Unit 3이 선택되었습니다.")

    def unit4_button_clicked(self):
        print(f"Unit 4이 선택되었습니다.")
        
    def unit5_button_clicked(self):
        print(f"Unit 5이 선택되었습니다.")

    def unit6_button_clicked(self):
        print(f"Unit 6이 선택되었습니다.")

    def unit7_button_clicked(self):
        print(f"Unit 7이 선택되었습니다.")

    def unit8_button_clicked(self):
        print(f"Unit 8이 선택되었습니다.")

    def unit9_button_clicked(self):
        print(f"Unit 9이 선택되었습니다.")
        
    def unit10_button_clicked(self):
        print(f"Unit 10이 선택되었습니다.")

    def unit11_button_clicked(self):
        print(f"Unit 11이 선택되었습니다.")    

    def unit12_button_clicked(self):
        print(f"Unit 12이 선택되었습니다.")

    def unit13_button_clicked(self):
        print(f"Unit 13이 선택되었습니다.")

    def unit14_button_clicked(self):
        print(f"Unit 14이 선택되었습니다.")

    def unit15_button_clicked(self):
        print(f"Unit 15이 선택되었습니다.")

    # setupUi
    def retranslateUi(self, UserUnitUI):
        UserUnitUI.setWindowTitle(QtCore.QCoreApplication.translate("UserUnitUI", u"MainWindow", None))
        self.back_button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"\ub4a4\ub85c\uac00\uae30", None))
        self.menu_name.setHtml(QtCore.QCoreApplication.translate("UserUnitUI", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Gulim'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'.AppleSystemUIFont'; font-size:20pt; font-weight:696;\">Part1</span></p></body></html>", None))
        self.home_button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"\ud648", None))
        self.unit1_button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"Unit 1", None))
        self.unit2_button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"Unit 2", None))
        self.unit3_button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"Unit 3", None))
        self.unit4_button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"Unit 4", None))
        self.unit5_button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"Unit 5", None))
        self.unit6_button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"Unit 6", None))
        self.unit7_button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"Unit 7", None))
        self.unit8_button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"Unit 8", None))
        self.unit9_button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"Unit 9", None))
        self.unit10_button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"Unit 10", None))
        self.unit11_Button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"Unit 11", None))
        self.unit12_Button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"Unit 12", None))
        self.unit13_Button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"Unit 13", None))
        self.unit14_Button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"Unit 14", None))
        self.unit15_Button.setText(QtCore.QCoreApplication.translate("UserUnitUI", u"Unit 15", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UserunitUI = QtWidgets.QMainWindow()
    ui = Ui_UserUnitUI()
    ui.setupUi(UserunitUI)
    UserunitUI.show()
    sys.exit(app.exec())