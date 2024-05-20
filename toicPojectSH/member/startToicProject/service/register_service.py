from repository.user_repository import UserRepository
from entity.user_entity import UserEntity

class RegisterService:
    def __init__(self):
        self.user_repository = UserRepository()

    def register_user(self, user_id, password, nickname):
        if len(user_id) < 4 or len(user_id) > 12:
            return False, "아이디는 4자 이상, 12자 이하로 입력해주세요"
        if self.user_repository.find_by_id(user_id):
            return False, "이미 존재하는 아이디입니다."
        user = UserEntity(user_id, nickname, password)
        success = self.user_repository.save(user)
        if success:
            return True, "회원가입에 성공했습니다."
        else:
            return False, "회원가입에 실패했습니다."
 

    def check_user_id(self, user_id):
        # 아이디가 데이터베이스에 존재하는지 확인
        if len(user_id) < 4 or len(user_id) > 12:
            return False, "아이디는 4자 이상, 12자 이하로 입력해주세요"
        user = self.user_repository.find_by_id(user_id)
        if user:
            return False, "이미 존재하는 아이디입니다."
        else:
            return True, "사용 가능한 아이디입니다."

