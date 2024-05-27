from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

app = QApplication([])

widget = QWidget()
layout = QVBoxLayout(widget)

button = QPushButton()
button.setFixedSize(100, 50)  # 버튼 크기 조정
button.setText("Your long text here with wrapping")
button.setStyleSheet("QPushButton { text-align: center; }")  # 텍스트 가운데 정렬
button.setWordWrap(True)  # 이제 버튼에 텍스트가 많을 경우 자동으로 줄 바꿈됩니다.

layout.addWidget(button)

widget.show()
app.exec()
