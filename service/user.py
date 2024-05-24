class User():
    def __init__(self, userId, userPassword="", userNickname="", userGoal=3, is_admin=0):
        self._userId = userId
        self._userPassword = userPassword
        self._userNickname = userNickname
        self._userGoal = userGoal
        self._is_admin = is_admin

    # userId에 대한 getter와 setter
    @property
    def userId(self):
        return self._userId

    @userId.setter
    def userId(self, value):
        self._userId = value

    # userNickname에 대한 getter와 setter
    @property
    def userNickname(self):
        return self._userNickname

    @userNickname.setter
    def userNickname(self, value):
        self._userNickname = value

    # userPassword에 대한 getter와 setter
    @property
    def userPassword(self):
        return self._userPassword

    @userPassword.setter
    def userPassword(self, value):
        self._userPassword = value

    # isAdmin에 대한 getter와 setter
    @property
    def is_admin(self):
        return self._is_admin

    @is_admin.setter
    def isAdmin(self, value):
        self._is_admin = value

    # userGoal에 대한 getter와 setter
    @property
    def userGoal(self):
        return self._userGoal
    
    @userGoal.setter
    def userGoal(self, value):
        self._userGoal = value

    def toUserEntity(user_data):
        # 데이터베이스에서 가져올 때 id, nickname, password, ... 순서로 나옴
        return User(user_data[0], user_data[2], user_data[1], user_data[3], user_data[4])

    def toUserData(self):
        return (self.userId, self.userPassword, self.userNickname, self.userGoal, self.is_admin)


