from BookmarkWordNote import BookmarkWordNote
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == "__main__": # UI 실행 코드
    app = QApplication(sys.argv)
    reviewWordNote = BookmarkWordNote("justID")
    app.exec()