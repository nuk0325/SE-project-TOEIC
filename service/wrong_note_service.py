from word_note import WordNote
from goto_service import Goto

class WrongNote(WordNote) :
    def __init__(self,user) :
        self.user = user
        self._titleName = "오답노트"
        self._testName = "오답노트 테스트 시작"
        self._testChoice = False
        self.db = self._makeDBobj()
        self._wordIdxList = self.db.getWrongWordList(self.user)
        self._wordList = self._returnWordList()
        
        self.main()

        self.goto = Goto()


    def use_goBack(self) :
        self._dbClose()
        self.goto.gotoMyPage(self.user)
    
    def use_gotoSelectTest(self) :
        self._dbClose()
        self.goto.gotoWrongNoteTest(self.user, self._wordIdxList, self._testChoice)