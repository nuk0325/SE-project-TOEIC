from WordNote import WordNote
from Goto import Goto

class AfterTestWordNote(WordNote) :
    def __init__(self, user, wordIdxList, anotherList, option) :
        self.user = user
        self._anotherList = anotherList
        self._titleName = self._getTitle(option)
        self._testName = "홈으로 가기"
        self._wordIdxList = wordIdxList
        self.db = self._makeDBobj()
        self._wordList = self._returnWordList()
        self.main()

    def _getTitle(self, option) :
        if option == "correct" :
            return "맞힌 단어장"
        elif option == "wrong" :
            return "틀린 단어장"
        else :
            print("AfterTestWordNote Option Error")
    
    def use_goBack(self) :
        Goto.goto

    def use_gotoSelectTest(self) :
        Goto.gotoHome(self.user)

