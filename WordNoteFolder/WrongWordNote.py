from WordNote import WordNote

class WrongWordNote(WordNote) :
    def __init__(self,user) :
        self.user = user
        self._titleName = "오답노트"
        self._testName = "오답노트 테스트 시작"
        self._testChoice = False
        self.db = self._makeDBobj()
        self._wordIdxList = self.db.getWrongWordList()
        self._wordList = self._returnWordList()
        self.main()