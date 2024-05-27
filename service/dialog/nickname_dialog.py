# -*- coding: utf-8 -*-

from PyQt6.QtWidgets import QDialog, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox

class NicknameDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.setWindowTitle("닉네임 변경")

        self.parent = parent

        self.input = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(QLabel("새로운 닉네임"))
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
            self.parent.changeNickname(newUserNickname)
            self.close()
