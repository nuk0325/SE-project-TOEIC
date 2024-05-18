import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

from UI.reviewTestUI import ReviewTestUI

class ReviewTest(QMainWindow):
    def __init__(self, wordList, unitNum, partNum):
        super().__init__()
        self.ui = ReviewTestUI()
        self.ui.setupUi(self)

        self.wordList = wordList
        self.unitNum = unitNum
        self.partNum = partNum

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReviewTest()
    window.show()
    sys.exit(app.exec())
