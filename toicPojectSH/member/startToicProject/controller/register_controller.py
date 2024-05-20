from PyQt6.QtWidgets import QMessageBox, QMainWindow
from service.register_service import RegisterService
from ui.loginPageUi import Ui_loginPage#삭제

class RegisterController:
    id_check_result = False
    user_id = ""
    def __init__(self, register_ui):
        self.register_ui = register_ui
        self.register_service = RegisterService()
        self.setup_connections()

    def setup_connections(self):
        self.register_ui.userRegisterBtn.clicked.connect(self.register_user)
        self.register_ui.checkIdBtn.clicked.connect(self.check_user_id)
        self.register_ui.backBtn.clicked.connect(self.goback)

    
    # LoginController의 기능 사용
    def goback(self):
        #Goto.gotoLogin()으로 아래 대체
        from controller.login_controller import LoginController
        self.login_window = QMainWindow()
        self.login_ui = Ui_loginPage()
        self.login_ui.setupUi(self.login_window)
        self.login_controller = LoginController(self.login_ui, self.login_window)
        self.login_window.show()  # 회원가입 페이지를 보여줌
        self.register_window.close()  # 로그인 페이지 종료
        pass

    def register_user(self):
        user_id = self.register_ui.id.text()
        password = self.register_ui.password.text()
        nickname = self.register_ui.nicname.text()

        if self.id_check_result and user_id== self.user_id:
            success, message = self.register_service.register_user(user_id, nickname, password)
            if success:
                QMessageBox.information(None, "회원가입 결과", message)
                # 회원가입 성공 시 로그인페이지로 이동
                #Goto.gotoLogin()
                pass
            if success:
                self.register_window.close()
        else:
            QMessageBox.information(None, "회원가입 실패", "아이디 중복 검사를 확인해주세요")
    def check_user_id(self):
        self.user_id = self.register_ui.id.text()
        user_id = self.register_ui.id.text()
        success, message = self.register_service.check_user_id(user_id)
        self.id_check_result = success
        QMessageBox.information(None, "아이디 중복 검사", message)

