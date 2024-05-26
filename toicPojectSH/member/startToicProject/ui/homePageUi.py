# Form implementation generated from reading ui file 'C:\Users\CHO\toicProject\hun\toicPojectSH\member\homePage.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_homePage(object):
    def setupUi(self, homePage):
        homePage.setObjectName("homePage")
        homePage.resize(360, 600)
        homePage.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(parent=homePage)
        self.centralwidget.setObjectName("centralwidget")
        self.menuBase = QtWidgets.QWidget(parent=self.centralwidget)
        self.menuBase.setGeometry(QtCore.QRect(0, 0, 360, 58))
        self.menuBase.setStyleSheet("background-color:rgba(253, 213, 51, 0.97)")
        self.menuBase.setObjectName("menuBase")
        self.titleName = QtWidgets.QLabel(parent=self.menuBase)
        self.titleName.setGeometry(QtCore.QRect(170, 10, 41, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.titleName.setFont(font)
        self.titleName.setStyleSheet("font: 700 20pt \"맑은 고딕\";\n"
"")
        self.titleName.setObjectName("titleName")
        self.toStudyBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.toStudyBtn.setGeometry(QtCore.QRect(60, 340, 240, 40))
        self.toStudyBtn.setStyleSheet("background-color:rgb(255, 240, 129)")
        self.toStudyBtn.setObjectName("toStudyBtn")
        self.toTotalTestBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.toTotalTestBtn.setGeometry(QtCore.QRect(60, 400, 240, 40))
        self.toTotalTestBtn.setStyleSheet("background-color:rgb(255, 240, 129)")
        self.toTotalTestBtn.setObjectName("toTotalTestBtn")
        self.toMyPageBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.toMyPageBtn.setGeometry(QtCore.QRect(60, 460, 240, 40))
        self.toMyPageBtn.setStyleSheet("background-color:rgb(255, 240, 129)")
        self.toMyPageBtn.setObjectName("toMyPageBtn")
        self.dogProgressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.dogProgressBar.setGeometry(QtCore.QRect(40, 280, 311, 16))
        self.dogProgressBar.setProperty("value", 24)
        self.dogProgressBar.setObjectName("dogProgressBar")
        self.dogProgressText = QtWidgets.QLabel(parent=self.centralwidget)
        self.dogProgressText.setGeometry(QtCore.QRect(20, 290, 320, 20))
        self.dogProgressText.setObjectName("dogProgressText")
        self.dogProgressText.setText("토익멍 성장까지    0/24")  #초기텍스트
        self.dogProgressText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dogProgressText.setWordWrap(True)
        self.goalProgressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.goalProgressBar.setGeometry(QtCore.QRect(40, 310, 311, 16))
        self.goalProgressBar.setProperty("value", 24)
        self.goalProgressBar.setObjectName("goalProgressBar")
        self.goalProgressText = QtWidgets.QLabel(parent=self.centralwidget)
        self.goalProgressText.setGeometry(QtCore.QRect(20, 320, 320, 20))
        self.goalProgressText.setObjectName("goalProgressText")
        self.goalProgressText.setText("금일 학습유닛    0/0")  #초기텍스트
        self.goalProgressText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.goalProgressText.setWordWrap(True)
        self.studyHelpBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.studyHelpBtn.setGeometry(QtCore.QRect(310, 350, 31, 28))
        self.studyHelpBtn.setStyleSheet("font: 6pt \"맑은 고딕\";")
        self.studyHelpBtn.setObjectName("studyHelpBtn")
        self.totalTestHelpBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.totalTestHelpBtn.setGeometry(QtCore.QRect(310, 410, 31, 28))
        self.totalTestHelpBtn.setStyleSheet("font: 6pt \"맑은 고딕\";")
        self.totalTestHelpBtn.setObjectName("totalTestHelpBtn")
        self.myPageHelpBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.myPageHelpBtn.setGeometry(QtCore.QRect(310, 470, 31, 28))
        self.myPageHelpBtn.setStyleSheet("font: 6pt \"맑은 고딕\";")
        self.myPageHelpBtn.setObjectName("myPageHelpBtn")
        
        # Add cheat button at the top right corner
        self.cheatBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cheatBtn.setGeometry(QtCore.QRect(355, 58, 5, 5))  # 위치와 크기 설정
        self.cheatBtn.setObjectName("cheatBtn")
        
        # Add speech balloon image
        self.speechBalloonImage = QtWidgets.QLabel(self.centralwidget)
        self.speechBalloonImage.setGeometry(QtCore.QRect(0, 60, 200, 100))  # QLabel의 크기를 조정하세요.
        self.speechBalloonImage.setPixmap(QtGui.QPixmap("image/speech_balloon.jpg"))
        self.speechBalloonImage.setScaledContents(True)  # 이미지가 QLabel 크기에 맞게 스케일링되도록 설정
        self.speechBalloonImage.setObjectName("speechBalloonImage")

        # Add text overlay on speech balloon
        self.speechBalloonText = QtWidgets.QLabel(self.speechBalloonImage)
        self.speechBalloonText.setGeometry(QtCore.QRect(15, 20, 148, 70))  # Adjust size and position inside the balloon
        self.speechBalloonText.setObjectName("speechBalloonText")
        self.speechBalloonText.setText("unitTest를 통과할 때마다 게이지가 올라갑니다")  #초기텍스트
        self.speechBalloonText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.speechBalloonText.setWordWrap(True)

        # Add dog image based on level
        self.dogImage = QtWidgets.QLabel(self.centralwidget)
        self.dogImage.setGeometry(QtCore.QRect(130, 180, 100, 70))
        self.dogImage.setObjectName("dogImage")
        self.dogImage.setScaledContents(True)
        self.dogImage.raise_()  # 이미지를 맨 앞으로 가져옴




        homePage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=homePage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 26))
        self.menubar.setObjectName("menubar")
        homePage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=homePage)
        self.statusbar.setObjectName("statusbar")
        homePage.setStatusBar(self.statusbar)

        self.retranslateUi(homePage)
        QtCore.QMetaObject.connectSlotsByName(homePage)

    def retranslateUi(self, homePage):
        _translate = QtCore.QCoreApplication.translate
        homePage.setWindowTitle(_translate("homePage", "MainWindow"))
        self.titleName.setText(_translate("homePage", "홈"))
        self.toStudyBtn.setText(_translate("homePage", "학습하기"))
        self.toTotalTestBtn.setText(_translate("homePage", "테스트 시작하기"))
        self.toMyPageBtn.setText(_translate("homePage", "마이페이지"))
        self.studyHelpBtn.setText(_translate("homePage", "도움말"))
        self.totalTestHelpBtn.setText(_translate("homePage", "도움말"))
        self.myPageHelpBtn.setText(_translate("homePage", "도움말"))

    def setDogImageBasedOnLevel(self, dog_level):
        base_width = 100
        base_height = 70
        scale_factor = 1 + 0.1 * (dog_level - 1)
        new_width = int(base_width * scale_factor)
        new_height = int(base_height * scale_factor)
        print(f"Loading image: image/dog_level{dog_level}.png")  # Add this line for debugging
        self.dogImage.setGeometry(QtCore.QRect(180 - new_width // 2, 250 - new_height, new_width, new_height))
        pixmap = QtGui.QPixmap(f"image/dog_level{dog_level}.png")
        if not pixmap.isNull():  
            self.dogImage.setPixmap(pixmap)
        else:
            print("Error: Failed to load image")

    def updateSpeechBalloonText(self, new_text):
        self.speechBalloonText.setText(new_text)

    def updateDogProgressText(self, new_text):
        self.dogProgressText.setText(new_text)

    def updateGoalProgressText(self, new_text):
        self.goalProgressText.setText(new_text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homePage = QtWidgets.QMainWindow()
    ui = Ui_homePage()
    ui.setupUi(homePage)
    homePage.show()
    sys.exit(app.exec())

