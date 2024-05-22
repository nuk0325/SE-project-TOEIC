from repository.user_repository import UserRepository
from entity.user_entity import UserEntity
import datetime

class HomeService:
    def __init__(self, user: UserEntity):
        self.user_repository = UserRepository()
        self.user = user
        self.today_learned_unit = user.today_learned_unit
        self.last_date = user.last_date
        self.reset_today_goal_if_new_day()

    def reset_today_goal_if_new_day(self):
        user =self.user_repository.find_by_id(self.user.userId)
        #오류 검증할 것 (날짜가 변경되었는지 확인)
        if not datetime.date.today()==user.last_date:
            self.today_learned_unit = 0
            self.last_date = datetime.date.today()
            self.user.last_date = datetime.date.today()
            self.user = self.user_repository.update(self.user)
        else:
            
    
    def printMotivationSentence():

        pass

    def printGoalProgressGage(userGoal):
        user.userGoal
        pass

    def printDogProgressGage(userGoal):
        
        pass

    def showHelpMesseage():

        pass

