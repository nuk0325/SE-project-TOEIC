from repository.user_repository import UserRepository
from entity.user_entity import UserEntity
import datetime

class HomeService:
    def __init__(self, user: UserEntity):
        self.user_repository = UserRepository()
        self.user = user
        self.last_date = user.last_date
        self.runIfOpenHome()
        
        
        
    def runIfOpenHome(self):
        self.checkDayChange()
        

    def checkDayChange(self):  
        user =self.user_repository.find_by_id(self.user.userId)
        #오류 검증할 것 (날짜가 변경되었는지 확인)
        last_date = datetime.datetime.strptime(user.last_date, '%Y-%m-%d').date()
        if not last_date == datetime.date.today():
            self.today_learned_unit = 0
            self.last_date = datetime.date.today()
            self.user.last_date = datetime.date.today()
            self.user = self.user_repository.update(self.user)
        else:
            self.today_learned_unit = user.today_learned_unit
            
    
    def printMotivationSentence():

        pass

    def printGoalProgressGage(userGoal):
        user.userGoal
        pass

    def printDogProgressGage(userGoal):
        
        pass

    def showHelpMesseage():

        pass

