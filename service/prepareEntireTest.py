import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from UI.prepareEntireTestUI import Ui_MainWindow  

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
