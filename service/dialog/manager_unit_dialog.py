from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QHBoxLayout, QPushButton

class ManagerUnitDialog(QDialog):
    def __init__(self, parent, sent, boolean):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("알림")

        layout = QVBoxLayout()
        layout.addWidget(QLabel(sent))

        buttonLayout = QHBoxLayout()

        yesBtn = QPushButton("확인")
        yesBtn.clicked.connect(lambda: self.yes(boolean))
        buttonLayout.addWidget(yesBtn)

        if boolean :
            yesBtn.setText("예")
            noBtn = QPushButton("아니오")
            noBtn.clicked.connect(self.no)
            buttonLayout.addWidget(noBtn)

        layout.addLayout(buttonLayout)
        self.setLayout(layout)

    def yes(self, boolean):
        self.close()
        if boolean :
            self.parent.deleteWord()
        
    def no(self):
        self.close()