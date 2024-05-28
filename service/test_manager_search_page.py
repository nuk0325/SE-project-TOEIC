# 파일: test_manager_search_page.py

from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from UI.manager_search_page_ui import Ui_managerSearchPage
from manager_search_page_service import managerSearchPageService

class TestManagerSearchPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_managerSearchPage()
        self.ui.setupUi(self)
        self.service = managerSearchPageService(self.ui)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TestManagerSearchPage()
    window.show()
    sys.exit(app.exec())
