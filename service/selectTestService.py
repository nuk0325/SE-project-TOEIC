import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from selectTestUI import Ui_MainWindow  # reviewTestUI UI 코드가 있는 파일명

class SelectTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SelectTest()
    window.show()
    sys.exit(app.exec())
