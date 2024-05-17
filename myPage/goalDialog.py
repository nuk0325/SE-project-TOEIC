from PyQt6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox, QComboBox

class GoalDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("학습 목표 수정")

        self.input = QComboBox()
        self.input.addItem("1")
        self.input.addItem("2")
        self.input.addItem("3")
        self.input.addItem("4")
        self.input.addItem("5")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("목표 학습 유닛 수"))
        layout.addWidget(self.input)

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
        newUserNickname = self.input.text()
        
        if newUserNickname == "":
            msg = QMessageBox()
            msg.setText("새로운 닉네임을 입력해주세요")

            okBtn = QPushButton("확인")
            msg.addButton(okBtn, QMessageBox.ButtonRole.YesRole)
            
            msg.exec()
        else :
            from myPageService import MyPage
            MyPage.changePassword(newUserNickname)
            self.close()
