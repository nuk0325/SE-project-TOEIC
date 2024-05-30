
from PyQt6.QtWidgets import QApplication
import sys
from add_by_manager_service import AddByManagerService
'''
class TestUpdateByManager(AddByManagerService):
    def __init__(self, line_num):
        super().__init__(line_num)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    line_num = 10  # Example line number to initialize the service
    window = TestUpdateByManager(line_num)
    window.show()
    sys.exit(app.exec())

'''# 파일: test_update_by_manager.py

from PyQt6.QtWidgets import QApplication
import sys
from update_by_manager_service import UpdateByManagerService

class TestUpdateByManager(UpdateByManagerService):
    def __init__(self, line_num):
        super().__init__(line_num)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    line_num = 10  # Example line number to initialize the service
    window = TestUpdateByManager(line_num)
    window.show()
    sys.exit(app.exec())

