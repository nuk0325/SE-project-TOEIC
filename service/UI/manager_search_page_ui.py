from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox, QPushButton, QApplication, QWidget, QScrollArea

class Ui_managerSearchPage(object):
    def setupUi(self, managerSearchPage):
        self.WordButtonNum = 0
        managerSearchPage.setObjectName("managerSearchPage")
        managerSearchPage.resize(360, 608)
        managerSearchPage.setStyleSheet("background-color:rgb(220, 220, 220)\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=managerSearchPage)
        self.centralwidget.setObjectName("centralwidget")
        self.menuBase = QtWidgets.QWidget(parent=self.centralwidget)
        self.menuBase.setGeometry(QtCore.QRect(0, 0, 360, 58))
        self.menuBase.setStyleSheet("background-color:rgba(50, 50, 50,1)")
        self.menuBase.setObjectName("menuBase")
        self.titleName = QtWidgets.QLabel(parent=self.menuBase)
        self.titleName.setGeometry(QtCore.QRect(110, 10, 151, 41))
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
        self.logoutBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.logoutBtn.setGeometry(QtCore.QRect(10, 70, 341, 31))
        self.logoutBtn.setStyleSheet("background-color:rgb(70, 70, 70);\n"
"font: 10pt \"맑은 고딕\";\n"
"color: rgb(255, 255, 255);")
        self.logoutBtn.setAutoDefault(False)
        self.logoutBtn.setDefault(False)
        self.logoutBtn.setFlat(False)
        self.logoutBtn.setObjectName("logoutBtn")
        self.searchBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.searchBtn.setGeometry(QtCore.QRect(310, 110, 41, 41))
        self.searchBtn.setStyleSheet("background-color:rgb(220, 220, 220);\n"
"font: 12pt \"맑은 고딕\";\n"
"color: rgb(0,0,0);")
        self.searchBtn.setAutoDefault(False)
        self.searchBtn.setDefault(False)
        self.searchBtn.setFlat(False)
        self.searchBtn.setObjectName("searchBtn")
        self.toSearchEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.toSearchEdit.setGeometry(QtCore.QRect(10, 110, 291, 41))
        self.toSearchEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.toSearchEdit.setObjectName("toSearchEdit")

        # Scroll Area 추가 시작
        self.scrollArea = QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 170, 341, 400))
        self.scrollArea.setStyleSheet("background-color:rgb(220, 220, 220);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 321, 400))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        # Scroll Area 추가 끝

        self.verticalLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        managerSearchPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=managerSearchPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 26))
        self.menubar.setObjectName("menubar")
        managerSearchPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=managerSearchPage)
        self.statusbar.setObjectName("statusbar")
        managerSearchPage.setStatusBar(self.statusbar)


        self.retranslateUi(managerSearchPage)
        QtCore.QMetaObject.connectSlotsByName(managerSearchPage)
        
    def retranslateUi(self, managerSearchPage):
        _translate = QtCore.QCoreApplication.translate
        managerSearchPage.setWindowTitle(_translate("managerSearchPage", "MainWindow"))
        self.titleName.setText(_translate("managerSearchPage", "단어 관리"))
        self.menuBtn.setText(_translate("managerSearchPage", "메뉴"))
        self.logoutBtn.setText(_translate("managerSearchPage", "관리자 로그아웃"))
        self.searchBtn.setText(_translate("managerSearchPage", "검색"))

    def clearWordButtons(self):  # 기존버튼삭제
        while self.verticalLayout.count():
            child = self.verticalLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        self.WordButtonNum=0

    def createWordButton(self, partNum, unitNum, word):  # 검색한 단어 버튼에 출력
        button = QtWidgets.QPushButton(parent=self.scrollAreaWidgetContents)  # 부모를 scrollAreaWidgetContents로 변경
        button.setStyleSheet("background-color:rgb(170, 170, 170);\n"
                              "font: 10pt \"맑은 고딕\";\n"
                              "color: rgb(255, 255, 255);")
        button.setAutoDefault(False)
        button.setDefault(False)
        button.setFlat(False)
        button.setObjectName(f"toWordBtn_{self.WordButtonNum}")
        button.setText(f"part{partNum} unit{unitNum}\n{word}")

        self.verticalLayout.addWidget(button)  # 버튼을 레이아웃의 맨 위에 추가
        self.WordButtonNum += 1
        self.scrollArea.verticalScrollBar().setValue(0)  # 스크롤 위치를 최상단으로 설정
        return button

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    managerSearchPage = QtWidgets.QMainWindow()
    ui = Ui_managerSearchPage()
    ui.setupUi(managerSearchPage)
    managerSearchPage.show()
    sys.exit(app.exec())