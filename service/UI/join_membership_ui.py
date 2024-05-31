# Form implementation generated from reading ui file 'C:\Users\CHO\toicProject\hun\toicPojectSH\member\register.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class JoinMembershipUI(object):
    def setupUi(self, registerPage):
        registerPage.setObjectName("registerPage")
        registerPage.resize(360, 600)
        registerPage.setStyleSheet("background-color:rgb(255, 255, 255)\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=registerPage)
        self.centralwidget.setObjectName("centralwidget")
        self.userRegisterBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.userRegisterBtn.setGeometry(QtCore.QRect(60, 350, 240, 40))
        self.userRegisterBtn.setStyleSheet("background-color:rgb(255, 240, 129)")
        self.userRegisterBtn.setObjectName("userRegisterBtn")
        self.id = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.id.setGeometry(QtCore.QRect(60, 170, 150, 40))
        self.id.setObjectName("id")
        self.password = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.password.setGeometry(QtCore.QRect(60, 220, 240, 40))
        self.password.setObjectName("password")
        self.menuBase = QtWidgets.QWidget(parent=self.centralwidget)
        self.menuBase.setGeometry(QtCore.QRect(0, 0, 360, 58))
        self.menuBase.setStyleSheet("background-color:rgba(253, 213, 51, 0.97)")
        self.menuBase.setObjectName("menuBase")
        self.titleName = QtWidgets.QLabel(parent=self.menuBase)
        self.titleName.setGeometry(QtCore.QRect(130, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.titleName.setFont(font)
        self.titleName.setStyleSheet("font: 700 20pt \"맑은 고딕\";\n"
"")
        self.titleName.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.titleName.setObjectName("titleName")
        self.backBtn = QtWidgets.QPushButton(parent=self.menuBase)
        self.backBtn.setGeometry(QtCore.QRect(0, 0, 60, 60))
        self.backBtn.setObjectName("backBtn")
        self.nicname = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.nicname.setGeometry(QtCore.QRect(60, 270, 240, 40))
        self.nicname.setObjectName("nicname")
        self.checkIdBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.checkIdBtn.setGeometry(QtCore.QRect(220, 170, 80, 40))
        self.checkIdBtn.setStyleSheet("background-color:rgb(193, 193, 193);\n"
"font: 7pt \"맑은 고딕\";")
        self.checkIdBtn.setAutoDefault(False)
        self.checkIdBtn.setDefault(False)
        self.checkIdBtn.setFlat(False)
        self.checkIdBtn.setObjectName("checkIdBtn")
        registerPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=registerPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 33))
        self.menubar.setObjectName("menubar")
        registerPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=registerPage)
        self.statusbar.setObjectName("statusbar")
        registerPage.setStatusBar(self.statusbar)

        self.retranslateUi(registerPage)
        QtCore.QMetaObject.connectSlotsByName(registerPage)

    def retranslateUi(self, registerPage):
        _translate = QtCore.QCoreApplication.translate
        registerPage.setWindowTitle(_translate("registerPage", "MainWindow"))
        self.userRegisterBtn.setText(_translate("registerPage", "회원가입"))
        self.id.setText(_translate("registerPage", "아이디"))
        self.password.setText(_translate("registerPage", "비밀번호"))
        self.titleName.setText(_translate("registerPage", "회원 가입"))
        self.backBtn.setText(_translate("registerPage", "뒤로가기"))
        self.nicname.setText(_translate("registerPage", "닉네임"))
        self.checkIdBtn.setText(_translate("registerPage", "아이디 중복 확인"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registerPage = QtWidgets.QMainWindow()
    ui = Ui_registerPage()
    ui.setupUi(registerPage)
    registerPage.show()
    sys.exit(app.exec())