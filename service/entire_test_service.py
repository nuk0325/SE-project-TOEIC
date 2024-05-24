import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from service.UI.entire_test_ui import EntireTestUI

class EntireTest(QMainWindow):
    def __init__(self, userNickname):
        super().__init__()
        self.ui = EntireTestUI()
        self.ui.setupUi(self)

        self.userNickname = userNickname
        print(self.userNickname)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EntireTestUI()
    window.show()
    sys.exit(app.exec())