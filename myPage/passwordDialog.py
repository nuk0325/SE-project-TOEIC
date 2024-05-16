from PyQt6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox
from myPageService import MyPage

class PasswordDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Dialog")

        # 세 개의 사용자 입력 창 생성
        self.input1 = QLineEdit()
        self.input2 = QLineEdit()
        self.input3 = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("기존 비밀번호"))
        layout.addWidget(self.input1)
        layout.addWidget(QLabel("새로운 비밀번호"))
        layout.addWidget(self.input2)
        layout.addWidget(QLabel("새로운 비밀번호 확인"))
        layout.addWidget(self.input3)

        buttonLayout = QHBoxLayout()
        cancelBtn = QPushButton("취소")
        cancelBtn.clicked.connect(self.cancel)
        saveBtn = QPushButton("저장")
        saveBtn.clicked.connect(self.save)
        buttonLayout.addWidget(cancelBtn)
        buttonLayout.addWidget(saveBtn)

        layout.addLayout(buttonLayout)
        self.setLayout(layout)

    def cancel(self):
        self.close()

    def save(self):
        checkUserPassword = self.input1.text()
        newUserPassword = self.input2.text()
        checkNewUserPassword = self.input3.text()

        if checkUserPassword == "" or newUserPassword == "" or checkNewUserPassword == "":
            msg = QMessageBox()
            msg.setText("정보를 모두 입력해주세요")

            okBtn = QPushButton("확인")
            msg.addButton(okBtn, QMessageBox.ButtonRole.YesRole)
            
            msg.exec()
        elif checkUserPassword : # checkUserPassword 확인
            pass
        elif newUserPassword != checkNewUserPassword : # newUserPassword == checkNewUserPassword 확인
            msg = QMessageBox()
            msg.setText("새로운 비밀번호가 일치하지 않습니다")

            okBtn = QPushButton("확인")
            msg.addButton(okBtn, QMessageBox.ButtonRole.YesRole)
            
            msg.exec()
        else :
            MyPage.changePassword(newUserPassword)
            self.close()
