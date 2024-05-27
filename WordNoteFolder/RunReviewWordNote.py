from ReviewWordNote import ReviewWordNote
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == "__main__": # UI 실행 코드
    app = QApplication(sys.argv)
    ReviewWordNote("justID", 2,1)
    app.exec()