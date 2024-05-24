from PyQt6.QtWidgets import QMessageBox, QMainWindow
from service.log_in_service import LogIn
from service.join_membership_service import JoinMembership
from join_membership_service import JoinMembership
from service.controller.join_memebsership_controller import RegisterController

class LoginController:
    def __init__(self, login_ui, login_window):
        self.login_ui = login_ui
        self.login_window = login_window
        self.login_service = LogIn()
        self.setup_connections()
    
    def setup_connections(self):
        self.login_ui.loginBtn.clicked.connect(self.login)
        self.login_ui.toRegisterPageBtn.clicked.connect(self.open_register_page)  # 이벤트 연결 추가

    def open_register_page(self):

        #Goto.gotoRegister()로 아래 대체
        
        self.register_window = QMainWindow()
        self.register_ui = JoinMembership()
        self.register_ui.setupUi(self.register_window)
        self.register_controller = RegisterController(self.register_ui)# RegisterController를 생성하고 UI와 연결
        self.register_window.show()  # 회원가입 페이지를 보여줌
        self.login_window.close()  # 로그인 페이지 종료

        

    def login(self):
        user_id = self.login_ui.id.text()
        password = self.login_ui.password.text()
        success, message = self.login_service.login_user(user_id, password)
        if success:
            print(message)
            # 로그인 성공 시 홈으로 이동
            #Goto.gotoHome()
            pass
        else:
            QMessageBox.information(None, "로그인 실패", message)
