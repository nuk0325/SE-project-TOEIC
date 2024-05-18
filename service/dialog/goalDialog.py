from PyQt6.QtWidgets import QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QComboBox
from PyQt6.QtCore import Qt

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

        msg1 = QLabel("목표 학습 유닛 수")
        msg1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        msg2 = QLabel("\n목표 학습 유닛 수를 설정합니다\n\n각 유닛의 테스트 문제를 모두 맞춰야\n해당 유닛을 학습한 것으로 측정됩니다\n\n설정한 목표 학습량만큼 학습하여\n강아지를 성장시켜보세요!")
        msg2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(msg1)
        layout.addWidget(self.input)
        layout.addWidget(msg2)

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
        from myPageService import MyPage

        newUserGoal = self.input.currentIndex() + 1
        MyPage.changeGoal(self, newUserGoal)
        self.close()

