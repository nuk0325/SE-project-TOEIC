# Form implementation generated from reading ui file 'C:\Users\CHO\toicProject\hun\SE-project-TOEIC\service\UI\add_by_manager_ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets

class ManagerAddWordUI(object):
    def setupUi(self, AddByManagerPage):
        AddByManagerPage.setObjectName("AddByManagerPage")
        AddByManagerPage.resize(360, 600)
        AddByManagerPage.setStyleSheet("background-color:rgb(255, 255, 255)\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=AddByManagerPage)
        self.centralwidget.setObjectName("centralwidget")
        self.menuBase = QtWidgets.QWidget(parent=self.centralwidget)
        self.menuBase.setGeometry(QtCore.QRect(0, 0, 360, 58))
        self.menuBase.setStyleSheet("background-color:rgb(50, 50, 50)")
        self.menuBase.setObjectName("menuBase")
        self.titleName = QtWidgets.QLabel(parent=self.menuBase)
        self.titleName.setGeometry(QtCore.QRect(120, 10, 151, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.titleName.setFont(font)
        self.titleName.setStyleSheet("font: 700 20pt \"맑은 고딕\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.titleName.setObjectName("titleName")
        self.menuBtn = QtWidgets.QPushButton(parent=self.menuBase)
        self.menuBtn.setGeometry(QtCore.QRect(300, 0, 60, 60))
        self.menuBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.menuBtn.setObjectName("menuBtn")
        self.backBtn = QtWidgets.QPushButton(parent=self.menuBase)
        self.backBtn.setGeometry(QtCore.QRect(0, 0, 60, 60))
        self.backBtn.setStyleSheet("color: rgb(255, 255, 255);")
        self.backBtn.setObjectName("backBtn")
        self.titleName_2 = QtWidgets.QLabel(parent=self.menuBase)
        self.titleName_2.setGeometry(QtCore.QRect(160, 50, 151, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.titleName_2.setFont(font)
        self.titleName_2.setStyleSheet("font: 700 20pt \"맑은 고딕\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.titleName_2.setObjectName("titleName_2")
        self.checkWordBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.checkWordBtn.setGeometry(QtCore.QRect(260, 180, 71, 41))
        self.checkWordBtn.setStyleSheet("background-color:rgb(220, 220, 220);\n"
"font: 8pt \"맑은 고딕\";\n"
"color: rgb(0,0,0);")
        self.checkWordBtn.setAutoDefault(False)
        self.checkWordBtn.setDefault(False)
        self.checkWordBtn.setFlat(False)
        self.checkWordBtn.setObjectName("checkWordBtn")
        self.word = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.word.setGeometry(QtCore.QRect(70, 180, 181, 41))
        self.word.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.word.setObjectName("word")
        self.exitBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exitBtn.setGeometry(QtCore.QRect(30, 490, 131, 41))
        self.exitBtn.setStyleSheet("background-color:rgb(70, 70, 70);\n"
"font: 10pt \"맑은 고딕\";\n"
"color: rgb(255, 255, 255);")
        self.exitBtn.setAutoDefault(False)
        self.exitBtn.setDefault(False)
        self.exitBtn.setFlat(False)
        self.exitBtn.setObjectName("exitBtn")
        self.addBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(200, 490, 131, 41))
        self.addBtn.setStyleSheet("background-color:rgb(70, 70, 70);\n"
"font: 10pt \"맑은 고딕\";\n"
"color: rgb(255, 255, 255);")
        self.addBtn.setAutoDefault(False)
        self.addBtn.setDefault(False)
        self.addBtn.setFlat(False)
        self.addBtn.setObjectName("addBtn")
        self.subTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.subTitle.setGeometry(QtCore.QRect(20, 120, 101, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.subTitle.setFont(font)
        self.subTitle.setStyleSheet("font: 700 11pt \"맑은 고딕\";\n"
"color: rgb(0, 0, 0\n"
");\n"
"")
        self.subTitle.setObjectName("subTitle")
        self.txt1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.txt1.setGeometry(QtCore.QRect(20, 180, 41, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.txt1.setFont(font)
        self.txt1.setStyleSheet("font: 700 9pt \"맑은 고딕\";\n"
"color: rgb(0, 0, 0\n"
");\n"
"")
        self.txt1.setObjectName("txt1")
        self.txt2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.txt2.setGeometry(QtCore.QRect(20, 240, 41, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.txt2.setFont(font)
        self.txt2.setStyleSheet("font: 700 9pt \"맑은 고딕\";\n"
"color: rgb(0, 0, 0\n"
");\n"
"")
        self.txt2.setObjectName("txt2")
        self.meaning = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.meaning.setGeometry(QtCore.QRect(70, 240, 261, 41))
        self.meaning.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.meaning.setObjectName("meaning")
        self.txt3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.txt3.setGeometry(QtCore.QRect(20, 300, 41, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.txt3.setFont(font)
        self.txt3.setStyleSheet("font: 700 9pt \"맑은 고딕\";\n"
"color: rgb(0, 0, 0\n"
");\n"
"")
        self.txt3.setObjectName("txt3")

        #예문 뜻 추가
        self.txt4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.txt4.setGeometry(QtCore.QRect(20, 380, 41, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.txt4.setFont(font)
        self.txt4.setStyleSheet("font: 700 9pt \"맑은 고딕\";\n"
"color: rgb(0, 0, 0\n"
");\n"
"")
        self.txt4.setObjectName("txt4")


        self.sentence = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.sentence.setGeometry(QtCore.QRect(70, 300, 261, 70))
        self.sentence.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sentence.setObjectName("sentence")
        
        #예문 뜻 추가
        self.sentenceMean = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.sentenceMean.setGeometry(QtCore.QRect(70, 390, 261, 70))
        self.sentenceMean.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sentenceMean.setObjectName("sentenceMean")

        
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 110, 320, 4))
        self.frame.setStyleSheet("background-color:rgb(180 ,180 ,180 )")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.unitName = QtWidgets.QLabel(parent=self.centralwidget)
        self.unitName.setGeometry(QtCore.QRect(20, 80, 61, 21))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.unitName.setFont(font)
        self.unitName.setStyleSheet("font: 700 12pt \"맑은 고딕\";\n"
"color: rgb(0, 0, 0\n"
");\n"
"")
        self.unitName.setObjectName("unitName")

        AddByManagerPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddByManagerPage)
        QtCore.QMetaObject.connectSlotsByName(AddByManagerPage)

        self.meaning.setWordWrapMode(QtGui.QTextOption.WrapMode.WordWrap)  # 뜻 입력 칸 자동 줄바꿈 설정
        self.sentence.setWordWrapMode(QtGui.QTextOption.WrapMode.WordWrap)  # 예문 입력 칸 자동 줄바꿈 설정
        self.sentenceMean.setWordWrapMode(QtGui.QTextOption.WrapMode.WordWrap)  # 예문 뜻 입력 칸 자동 줄바꿈 설정

    def retranslateUi(self, AddByManagerPage):
        _translate = QtCore.QCoreApplication.translate
        AddByManagerPage.setWindowTitle(_translate("AddByManagerPage", "MainWindow"))
        self.titleName.setText(_translate("AddByManagerPage", "단어 추가"))
        self.menuBtn.setText(_translate("AddByManagerPage", "메뉴"))
        self.backBtn.setText(_translate("AddByManagerPage", "뒤로"))
        self.checkWordBtn.setText(_translate("AddByManagerPage", "단어\n중복 확인"))
        self.exitBtn.setText(_translate("AddByManagerPage", "나가기"))
        self.addBtn.setText(_translate("AddByManagerPage", "추가하기"))
        self.subTitle.setText(_translate("AddByManagerPage", "단어 추가"))
        self.txt1.setText(_translate("AddByManagerPage", "단어"))
        self.txt2.setText(_translate("AddByManagerPage", "의미"))
        self.txt3.setText(_translate("AddByManagerPage", "예문"))
        #예문 뜻 추가
        self.txt4.setText(_translate("UpdateByManagerPage", "예문 뜻"))
        self.unitName.setText(_translate("AddByManagerPage", ""))

    def setUnitName(self, unitNum):
        _translate = QtCore.QCoreApplication.translate
        unit_text = f"Unit {unitNum}"
        self.unitName.setText(_translate("AddByManagerPage", unit_text))
