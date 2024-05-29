import sys
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication
#from UI.prepare_entire_test_ui import PrepareEntireTestUI
#from dialog.select_test_dialog import SelectTestDialog
#from goto_service import Goto
#from Goto import Goto

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QHBoxLayout, QPushButton
from EntireTestWordNote import EntireTestWordNote
from Goto import Goto
import random

class SelectEntireTestDialog(QDialog):
    def __init__(self, user, word_n, parent):
        super().__init__()
        self.user = user
        self.word_n = word_n #전체테스트 단어개수
        self.setWindowTitle("테스트 방식 선택")
        self.parent=parent

        layout = QVBoxLayout()
        layout.addWidget(QLabel("테스트 방식을 선택해주세요"))

        buttonLayout = QHBoxLayout()

        yesBtn = QPushButton("단어 테스트 시작")
        yesBtn.clicked.connect(self.yes)
        noBtn = QPushButton("뜻 테스트 시작")
        noBtn.clicked.connect(self.no)

        buttonLayout.addWidget(yesBtn)
        buttonLayout.addWidget(noBtn)

        layout.addLayout(buttonLayout)
        self.setLayout(layout)

    def yes(self):
        print("사용자가 '뜻으로 답하기'를 선택했습니다.")
        #전체테스트 단어장 생성
        EntireTestWordNote(self.user, False, self.word_n)
        self.parent.close()
        self.close()
        
    def no(self):
        print("사용자가 '영어로 답하기'를 선택했습니다.")
        #전체테스트 단어장 생성
        EntireTestWordNote(self.user, True, self.word_n)
        self.parent.close()
        self.close()


class PrepareEntireTestUI(object):
    def setupUi(self, MainWindow, correctWordNum, allWordNum):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(359, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(0, 1, 360, 60))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.back_button = QtWidgets.QPushButton(parent=self.frame_5)
        self.back_button.setGeometry(QtCore.QRect(0, 0, 60, 60))
        self.back_button.setObjectName("back_button")
        self.home_button = QtWidgets.QPushButton(parent=self.frame_5)
        self.home_button.setGeometry(QtCore.QRect(300, 0, 60, 60))
        self.home_button.setObjectName("home_button")
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow, f"{correctWordNum}/{allWordNum}")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


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
            <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">       </span></p>
            <p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt;">                   </span></p>
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


class PrepareEntireTest(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.ui = PrepareEntireTestUI()
        self.ui.setupUi(self, 3, 30)

        self.goto = Goto()
        self.user = user
        
        #self.goto = Goto()

         #button 클릭 이벤트
        self.ui.back_button.clicked.connect(self.back_button_clicked)#뒤로가기
        self.ui.home_button.clicked.connect(self.home_button_clicked)#홈
        self.ui.pushButton.clicked.connect(self.pushButton_clicked)#테스트 시작하기

    #button 클릭 이벤트
    def back_button_clicked(self):
        self.goto.gotoHome(self.user)
        self.close()
        
    def home_button_clicked(self):
        self.goto.gotoHome(self.user)
        self.close()
    
    def pushButton_clicked(self):
        selected_value = self.ui.comboBox.currentText()
        print(f"선택된 단어 수: {selected_value}")

        #SelectEntireTestDialog(self.user, selected_value, self)
        #dialog = SelectEntireTestDialog(self.user, selected_value, self)
        #dialog.exec_()  # QDialog 팝업을 모달로 실행합니다.

        # 전체 테스트 실행. 단어장을 생성하여 단어를 넘겨줌.
        self.close()
        testChose = bool(random.randint(0, 1)) # 뜻으로답할지, 영어로답할지 랜덤으로 결정
        EntireTestWordNote(self.user, testChose, selected_value)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrepareEntireTest("justID")
    window.show()
    #dialog = SelectEntireTestDialog("justID", 10, sys)
    #dialog.exec_()
    sys.exit(app.exec())
