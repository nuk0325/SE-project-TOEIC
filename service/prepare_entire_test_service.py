import sys
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication
from UI.prepare_entire_test_ui import PrepareEntireTestUI
from dialog.select_test_dialog import SelectTestDialog
from goto_service import Goto

class PrepareEntireTest(QMainWindow):
    def __init__(self, user):
        super().__init__()
        self.ui = PrepareEntireTestUI()
        self.ui.setupUi(self, 3, 30)

        self.user = user
        
        self.goto = Goto()

         #button 클릭 이벤트
        self.ui.back_button.clicked.connect(self.back_button_clicked)#뒤로가기
        self.ui.home_button.clicked.connect(self.home_button_clicked)#홈
        self.ui.pushButton.clicked.connect(self.pushButton_clicked)#테스트 시작하기

    #button 클릭 이벤트
    def back_button_clicked(self):
        self.goto.gotoHome(self.user)
        self.close()

        # msg_box = QMessageBox()
        # msg_box.setWindowTitle("Notification")
        # msg_box.setText("뒤로가기 버튼을 클릭했습니다.")
        # msg_box.setIcon(QMessageBox.Icon.Information)
        # msg_box.exec()
        
    def home_button_clicked(self):
        self.goto.gotoHome(self.user)
        self.close()

        # msg_box = QMessageBox()
        # msg_box.setWindowTitle("Notification")
        # msg_box.setText("홈 버튼을 클릭했습니다.")
        # msg_box.setIcon(QMessageBox.Icon.Information)
        # msg_box.exec()
    
    def pushButton_clicked(self):
        selected_value = self.ui.comboBox.currentText()
        print(f"선택된 단어 수: {selected_value}")

        SelectTestDialog()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrepareEntireTest()
    window.show()
    sys.exit(app.exec())
