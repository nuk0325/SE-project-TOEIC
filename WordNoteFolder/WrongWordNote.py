from WordNote import WordNote
from Goto import Goto

class WrongWordNote(WordNote) :
    def __init__(self,user) :
        self.user = user
        self._titleName = "오답노트"
        self._testName = "오답노트 테스트 시작"
        self._testChoice = False
        self.db = self._makeDBobj()
        self._wordIdxList = self.db.getWrongWordList(self.user)
        self._wordList = self._returnWordList()
        self.main()

    

    def getLabel(self) :
        return ""

    def use_goBack(self) :
        self._dbClose()
        Goto.gotoMypage()
    
    def use_gotoSelectTest(self) :
        self._dbClose()
        Goto.gotoWrongWordTest(self.user, self._wordIdxList, self._testChoice)