from UnitManage import UnitManage
from PyQt6.QtWidgets import QApplication
import sys

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    UnitManage("justID", 2, 1)
    app.exec()