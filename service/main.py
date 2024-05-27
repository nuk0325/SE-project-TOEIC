import sys
from PyQt6.QtWidgets import QApplication
from log_in_service import LogIn
######
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LogIn()
    window.show()
    sys.exit(app.exec())
