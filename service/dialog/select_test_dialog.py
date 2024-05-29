from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QHBoxLayout, QPushButton

class SelectTestDialog(QDialog):
    def __init__(self, parent, grand):
        super().__init__()
        self.grand = grand
        self.parent = parent
        self.setWindowTitle("테스트 방식 선택")

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
        self.grand.setTestChoice(False)
        self.close()
        self.parent.closeAndOpen("test")
        
    def no(self):
        print("사용자가 '영어로 답하기'를 선택했습니다.")
        self.grand.setTestChoice(True)
        self.close()
        self.parent.closeAndOpen("test")