# 파일: test_user_part.py

from PyQt6.QtWidgets import QApplication
import sys
from manager_part_service import ManagerPart  # user_part.py에 정의된 UserPart 클래스를 가져옵니다.
from user import User
if __name__ == "__main__":
    app = QApplication(sys.argv)
    user = User("111","111","111",3, 1)  # 실제 사용자 데이터를 여기에 전달하세요.
    window = ManagerPart(user)
    window.show()
    sys.exit(app.exec())
