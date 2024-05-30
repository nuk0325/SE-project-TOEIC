import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout

class InputLabelWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('입력 라벨 예제')
        
        # 입력란 생성
        self.input_label = QLineEdit(self)
        self.input_label.setPlaceholderText('여기에 입력하세요')
        
        # 결과 표시 라벨 생성
        self.result_label = QLabel(self)
        self.result_label.setText('입력된 텍스트: ')
        
        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)

        # 입력란의 텍스트가 변경될 때마다 결과 라벨 갱신
        self.input_label.textChanged.connect(self.update_result_label)

    def update_result_label(self, text):
        self.result_label.setText('입력된 텍스트: ' + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InputLabelWindow()
    window.show()
    sys.exit(app.exec())
