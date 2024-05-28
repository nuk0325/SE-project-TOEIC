import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from UI.manager_search_page_ui import Ui_managerSearchPage
from DB_manager import DBManager
from goto_service import Goto
import datetime, random
import csv
class managerSearchPageService:
    def __init__(self, ui):
        self.ui = ui
        #self.dataManager = DBManager()
        self.goto = Goto()

        # UI의 버튼 객체들을 가져옵니다.
        self.menuBtn = self.ui.menuBtn
        self.logoutBtn = self.ui.logoutBtn
        self.searchBtn = self.ui.searchBtn
        self.toSearchEdit = self.ui.toSearchEdit

        # 각 버튼에 클릭 이벤트를 연결합니다.
        self.menuBtn.clicked.connect(self.menu_btn_clicked)
        self.logoutBtn.clicked.connect(self.logout_btn_clicked)
        self.searchBtn.clicked.connect(self.search_btn_clicked)

    


    def menu_btn_clicked(self):
        print("menuBtn clicked")
        #self.goto.manager

    def logout_btn_clicked(self):
        print("logoutBtn clicked")
        self.goto.gotoLogIn()
        self.ui.close()

    def search_btn_clicked(self):
        # 검색 버튼 클릭 시 toSearchEdit에 입력된 단어 출력
        search_word = self.toSearchEdit.text()
        if len(search_word)<1:
            QMessageBox.information(None, "공백오류", "1글자 이상 입력하세요")
            return
        word_indices = self.find_word_indices(search_word)
        if len(word_indices)<1:
            QMessageBox.information(None, "단어 검색결과", "일치하는 단어가 없습니다.")
            return
        self.ui.clearWordButtons()  # 기존 단어 버튼 제거
        self.connect_word_buttons(word_indices)

    def add_word_button(self, word_index):
        # 단어 버튼을 생성하고 centralwidget에 추가
        button = self.ui.createWordButton(int(word_index[0]) // 120 + 1, int(word_index[0]) % 120 // 15 + 1, word_index[1])
        button.show()
        # 클릭 이벤트에 연결
        button.clicked.connect(lambda num=word_index: self.show_word_num(num))

    def connect_word_buttons(self, word_indices):
        for word_index in word_indices:
            self.add_word_button(word_index)

    def show_word_num(self, word_index):
        unitNum = word_index % 120 / 15 + 1
        print(unitNum)
        #self.goto.uinit(unitNum)

    def find_word_indices(self, word):
        file_path = "toeic_word_file.csv"
        word_indices = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if word in row[1]:
                    word_indices.append([int(row[0]),str(row[1])])

        return word_indices


'''
if __name__ == "__main__":
    import sys
    app =  QtWidgets.QApplication(sys.argv)
    managerSearchPage = QtWidgets.QMainWindow()
    ui = Ui_managerSearchPage()
    ui.setupUi(managerSearchPage)
    another = managerSearchPageService(ui)
    another.add_buttons()  # 버튼 추가
    managerSearchPage.show()
    sys.exit(app.exec())
'''