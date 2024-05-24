from PyQt6.QtWidgets import QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QLabel

class LogOutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("로그아웃")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("정말 로그아웃 하시겠습니까?"))

        buttonLayout = QHBoxLayout()

        yesBtn = QPushButton("네")
        yesBtn.clicked.connect(self.yes)
        noBtn = QPushButton("아니오")
        noBtn.clicked.connect(self.no)

        buttonLayout.addWidget(yesBtn)
        buttonLayout.addWidget(noBtn)

        layout.addLayout(buttonLayout)
        self.setLayout(layout)

    def yes(self):
        from my_page_service import MyPage
        myPage = MyPage()
        myPage.logOut()
        self.close()
        
    def no(self):
        self.close()
