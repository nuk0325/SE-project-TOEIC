import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from word import Word
from goto_service import Goto

class WordForManager(Word) :
    def __init__(self, parent, user, idx, db) :
        self.user = user
        self._idx = idx 
        self.db = db
        self.parent = parent
        self._wordName = self.db.getWord(idx, "word")
        self._meaning = self.db.getWord(idx, "meaning")
        self._sentence = self.db.getWord(idx, "sentence")
        self._sentMeaning = self.db.getWord(idx, "sentMeaning")

        self.goto = Goto()

    def changeWord(self) : # 함수 이름 맞춰서 쓰세요
        print("단어 수정 페이지로 이동")
        self.goto.gotoManagerUpdateWord(self._idx, self.parent.part, self.parent.unit, self.parent.user)
        pass

    def deleteWord(self) :
        print("단어 삭제")
        self._wordName = None
        self._meaning = None
        self._sentence = None
        self._sentMeaning = None
        self.db.deleteWord(self._idx)