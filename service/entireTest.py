import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from UI.entireTestUI import EntireTestUI

class EntireTest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = EntireTestUI()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EntireTestUI()
    window.show()
    sys.exit(app.exec())