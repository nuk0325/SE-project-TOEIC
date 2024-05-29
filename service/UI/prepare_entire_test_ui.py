from PyQt6 import QtWidgets, QtCore
from dialog.select_test_dialog import SelectTestDialog

class PrepareEntireTestUI(object):
    def setupUi(self, parent, correctWordNum, allWordNum):
        self.parent = parent

        parent.setObjectName("MainWindow")
        parent.resize(359, 600)
        self.centralwidget = QtWidgets.QWidget(parent=parent)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(0, 1, 360, 60))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.back_button = QtWidgets.QPushButton(parent=self.frame_5)
        self.back_button.setGeometry(QtCore.QRect(0, 0, 60, 60))
        self.back_button.setObjectName("back_button")
        self.back_button.clicked.connect(lambda: self.closeAndOpen("back"))

        self.home_button = QtWidgets.QPushButton(parent=self.frame_5)
        self.home_button.setGeometry(QtCore.QRect(300, 0, 60, 60))
        self.home_button.setObjectName("home_button")
        self.home_button.clicked.connect(lambda: self.closeAndOpen("home"))

        self.textBrowser = QtWidgets.QTextBrowser(parent=self.frame_5)
        self.textBrowser.setGeometry(QtCore.QRect(60, 0, 240, 60))
        self.textBrowser.setObjectName("textBrowser")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 509, 360, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 361, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.showPopUp)

        self.verticalLayout.addWidget(self.pushButton)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 60, 360, 261))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=self.frame_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 20, 321, 221))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.frame_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 320, 360, 191))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(parent=self.frame_3)
        self.label.setGeometry(QtCore.QRect(100, 20, 151, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(parent=self.frame_3)
        self.comboBox.setGeometry(QtCore.QRect(100, 40, 141, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        parent.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=parent)
        self.statusbar.setObjectName("statusbar")
        parent.setStatusBar(self.statusbar)

        self.retranslateUi(parent, f"{correctWordNum}/{allWordNum}")
        QtCore.QMetaObject.connectSlotsByName(parent)


    #ui 모양 할당
    def retranslateUi(self, MainWindow, pre_score: str):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.back_button.setText(_translate("MainWindow", "뒤로가기"))
        self.home_button.setText(_translate("MainWindow", "Home"))


        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "hr { height: 1px; border-width: 0; }\n"
            "li.unchecked::marker { content: \"\\2610\"; }\n"
            "li.checked::marker { content: \"\\2612\"; }\n"
            "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:5pt; ;\"> </span></p></body></html>"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">테스트 시작하기</span></p></body></html>"))
        
        textBrowser2_html = f"""
            <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
            <html><head><meta name="qrichtext" content="1" /><meta charset="utf-8" /><style type="text/css">
            p, li {{ white-space: pre-wrap;}}
            hr {{ height: 1px; border-width: 0; }}
            li.unchecked::marker {{ content: "\\2610"; }}
            i.checked::marker {{ content: "\\2612"; }}
            </style></head><body style=" font-family:'.AppleSystemUIFont'; font-size:5pt; font-weight:10; font-style:normal;">
            <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">       테스트 시작하기에서는</span></p>
            <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">       전체 유닛의 1200개 단어에 대해</span></p>
            <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">       모의고사를 실시합니다</span></p>
            <p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;"><br /></p>
            <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">       모의고사를 실시할 단어의 개수를</span></p>
            <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">       직접 지정할 수 있습니다</span></p>
            <p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;"><br /></p>
            <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">       직전 테스트 결과</span></p>
            <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">                   {pre_score}</span></p>
            </body></html>
            """
        self.textBrowser_2.setHtml(_translate("MainWindow", textBrowser2_html))

        self.pushButton.setText(_translate("MainWindow", "테스트 시작하기"))

        self.label.setText(_translate("MainWindow", "모의고사를 실시할 단어 수"))
        self.comboBox.setItemText(0, _translate("MainWindow", "10"))
        self.comboBox.setItemText(1, _translate("MainWindow", "20"))
        self.comboBox.setItemText(2, _translate("MainWindow", "30"))
        self.comboBox.setItemText(3, _translate("MainWindow", "40"))
        self.comboBox.setItemText(4, _translate("MainWindow", "50"))

    def showPopUp(self) :
        popup = SelectTestDialog(self, self.parent)
        popup.exec()

    def closeAndOpen(self, option) :
        if option == "back" :
            self.parent.back_button_clicked()
        elif option == "home" :
            self.parent.home_button_clicked()
        elif option == "test" :
            self.parent.pushButton_clicked()
        else :
            print("잘못된 입력입니다.")