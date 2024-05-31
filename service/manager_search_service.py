import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from UI.manager_search_ui import ManagerSearchUI
from DB_manager import DBManager
from goto_service import Goto

class ManagerSearch(QMainWindow):
    def __init__(self, user, option, partNum=None):
        super().__init__()
        self.ui = ManagerSearchUI()
        self.ui.setupUi(self)

        self.partNum = partNum
        self.user = user
        self.option = option

        self.dataManager = DBManager()
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
        self.goBack(self.option)

    def goBack(self, option):
        if option == "part":
            self.goto.gotoManagerPart(self.user)
        elif option == "unit":
            self.goto.gotoManagerUnit(self.partNum, self.user)
        self.close()

    def logout_btn_clicked(self):
        print("logoutBtn clicked")
        self.goto.gotoLogIn()
        self.close()

    def search_btn_clicked(self):
        # 검색 버튼 클릭 시 toSearchEdit에 입력된 단어 출력
        search_word = self.ui.toSearchEdit.text()

        if len(search_word)<1:
            QMessageBox.information(None, "공백오류", "1글자 이상 입력하세요")
            return
        
        word_indices = self.find_word_indices(search_word)
        if len(word_indices) < 1:
            QMessageBox.information(None, "단어 검색결과", "일치하는 단어가 없습니다.")
            return
        self.ui.clearWordButtons()  # 기존 단어 버튼 제거
        self.connect_word_buttons(word_indices)

    def add_word_button(self, word_index):
        # 단어 버튼을 생성하고 centralwidget에 추가
        index =word_index[0]- 1
        part = index // 150 + 1
        unit = index % 150 //10 + 1
        button = self.ui.createWordButton(part, unit, word_index[1])
        button.show()
        # 클릭 이벤트에 연결
        print(f"Adding button for word_index: {word_index}")
        button.clicked.connect(self.create_show_word_num_lambda(word_index[0]))

    def create_show_word_num_lambda(self, word_index):
        return lambda: self.show_word_num(word_index)
    
    def connect_word_buttons(self, word_indices):
        for word_index in word_indices:
            self.add_word_button(word_index)

    def show_word_num(self, word_index):
        print(f"Button clicked with word_index: {word_index}")
        partNum = word_index // 150 + 1
        unitNum = word_index % 150 //10 + 1
        print(unitNum)
        self.goto.gotoManagerUnitWordNote(partNum, unitNum, self.user)
        self.close()

    def find_word_indices(self, word):
        reader = self.dataManager.selectNumAndWord()
        word_indices = []
        for row in reader:
            if word in row[1]:
                word_indices.append([int(row[0]),str(row[1])])

        return word_indices
    
        '''
        file_path = "toeic_word_file.csv"
        word_indices = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if word in row[1]:
                    word_indices.append([int(row[0]),str(row[1])])

        return word_indices
        '''


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