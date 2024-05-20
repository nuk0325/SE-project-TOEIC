class UserEntity:
    def __init__(self, userId, userPassword='', userNicname='사용자', userGoal=3, is_admin=0):
        self.__userId = userId
        self.__userPassword = userPassword
        self.__userNicname = userNicname
        self.__userGoal = userGoal
        self.__is_admin = is_admin
        

    # userId에 대한 getter와 setter
    @property
    def userId(self):
        return self.__userId

    @userId.setter
    def userId(self, value):
        self.__userId = value

    # userNicname에 대한 getter와 setter
    @property
    def userNicname(self):
        return self.__userNicname

    @userNicname.setter
    def userNicname(self, value):
        self.__userNicname = value

    # userPassword에 대한 getter와 setter
    @property
    def userPassword(self):
        return self.__userPassword

    @userPassword.setter
    def userPassword(self, value):
        self.__userPassword = value

    # is_admin에 대한 getter와 setter
    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, value):
        self.__is_admin = value

    # userGoal에 대한 getter와 setter
    @property
    def userGoal(self):
        return self.__userGoal

    @userGoal.setter
    def userGoal(self, value):
        self.__userGoal = value

    def toUserEntity(user_data):
        return UserEntity(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4])

    def toUserData(self):
        return (self.userId, self.userPassword, self.userNicname, self.userGoal, self.is_admin)


