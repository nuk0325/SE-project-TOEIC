from repository.user_repository import UserRepository

class LoginService:
    def __init__(self):
        self.user_repository = UserRepository()

    def login_user(self, user_id, password):
        user = self.user_repository.find_by_id(user_id)
        if user and user.userPassword == password:
            return True, "로그인 성공"
        else:
            return False, "아이디 또는 비밀번호가 올바르지 않습니다."
        
    