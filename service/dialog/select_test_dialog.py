import sys
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QPushButton

class SelectTestDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('사용자 정의 팝업창')
        self.setGeometry(300, 300, 300, 200)

        self.showPopup()

    def showPopup(self):
        # QMessageBox 생성
        msg_box = QMessageBox()
        msg_box.setWindowTitle("테스트 방식 선택")
        msg_box.setText("테스트 방식을 선택해주세요")

        # 사용자 정의 버튼 생성
        btn_meaning = QPushButton('뜻으로 답하기')
        btn_english = QPushButton('영어로 답하기')

        # 버튼을 QMessageBox에 추가
        msg_box.addButton(btn_meaning, QMessageBox.ButtonRole.YesRole)
        msg_box.addButton(btn_english, QMessageBox.ButtonRole.NoRole)

        msg_box.clickedButton()

        # 팝업창 실행 및 응답 저장
        self.response = msg_box.exec()

        # 사용자 응답에 따른 처리
        if msg_box.clickedButton() == btn_meaning:
            print("사용자가 '뜻으로 답하기'를 선택했습니다.")
        elif msg_box.clickedButton() == btn_english:
            print("사용자가 '영어로 답하기'를 선택했습니다.")
        
