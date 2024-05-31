import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from word import Word
from goto_service import Goto

class WordForManager(Word) :
    def __init__(self, user, idx, db) :
        self.user = user
        self._idx = idx 
        self.db = db
        self._wordName = self.db.getWord(idx, "word")
        self._meaning = self.db.getWord(idx, "meaning")
        self._sentence = self.db.getWord(idx, "sentence")
        self._sentMeaning = self.db.getWord(idx, "sentMeaning")

    def setWordName(self, wordName) :
        self._wordName = wordName
        self.db.setWord(self._idx, "word")

    def setMeaning(self, meaning) :
        self._meaning = meaning
        self.db.setWord(self._idx, "meaning")

    def setSentence(self, sentence) :
        self._sentence = sentence
        self.db.setSentence(self._idx, "sentence")

    def setSentMeaning(self, sentMeaning) :
        self._sentMeaning = sentMeaning
        self.db.setSentMeaning(self._idx, "sentMeaning")

    def changeWord(self):
        print("단어 수정 페이지로 이동")
        Goto().gotoManagerUpdateWord(self._idx, self.user)
        #self.close()


    def deleteWord(self) :
        print("단어 삭제")
        self._wordName = None
        self._meaning = None
        self._sentence = None
        self._sentMeaning = None
        self.db.deleteWord(self._idx)