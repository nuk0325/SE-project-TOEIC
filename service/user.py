class User:
    def __init__(self, userId, userPassword='', userNickname='사용자', userGoal=3, is_admin=0, last_date=0, today_learned_unit=0, total_learned_unit=0):
        self.__userId = userId
        self.__userPassword = userPassword
        self.__userNickname = userNickname
        self.__userGoal = userGoal
        self.__is_admin = is_admin
        self.__last_date = last_date
        self.__today_learned_unit = today_learned_unit
        self.__total_learned_unit = total_learned_unit
        
    # userId에 대한 getter와 setter
    @property
    def userId(self):
        return self.__userId

    @userId.setter
    def userId(self, value):
        self.__userId = value

    # userNickname에 대한 getter와 setter
    @property
    def userNickname(self):
        return self.__userNickname

    @userNickname.setter
    def userNicname(self, value):
        self.__userNickname = value

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

    # last_date에 대한 getter와 setter
    @property
    def last_date(self):
        return self.__last_date

    @last_date.setter
    def last_date(self, value):
        self.__last_date = value

    # today_learned_unit에 대한 getter와 setter
    @property
    def today_learned_unit(self):
        return self.__today_learned_unit

    @today_learned_unit.setter
    def today_learned_unit(self, value):
        self.__today_learned_unit = value

    # total_learned_unit에 대한 getter와 setter
    @property
    def total_learned_unit(self):
        return self.__total_learned_unit

    @total_learned_unit.setter
    def total_learned_unit(self, value):
        self.__total_learned_unit = value

    def toUserEntity(user_data):
        user = User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[6], user_data[7])
        return user

    def toUserData(self):
        return (self.userId, self.userPassword, self.userNickname, self.userGoal, self.is_admin, self.last_date, self.today_learned_unit, self.total_learned_unit)
    
    def toUpdateUserEntity(user_id, user_data):
        user = User(user_id, user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5], user_data[6])
        return user

    def toUpdateUserData(self):
        return ( self.userPassword, self.userNickname, self.userGoal, self.is_admin, self.last_date, self.today_learned_unit, self.total_learned_unit)
