from WrongWordNote import WrongWordNote
from PyQt6.QtWidgets import QApplication
import sys
##
if __name__ == "__main__": # UI 실행 코드
    app = QApplication(sys.argv)
    wrongWordNote = WrongWordNote()
    app.exec()