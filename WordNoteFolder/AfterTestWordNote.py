from WordNote import WordNote
from Goto import Goto

class AfterTestWordNote(WordNote) :
    def __init__(self, user, wordIdxList, anotherList, op1, op2) :
        self.user = user
        self._anotherList = anotherList
        self._titleName = self._getTitle(op1)
        self._testName = "홈으로 가기"
        self._wordIdxList = wordIdxList
        self.db = self._makeDBobj()
        self._wordList = self._returnWordList()
        self._op2 = op2 # 어디로 돌아가는지에 대한 옵션
        # review -> 복습 / wrong -> 오답 / fav -> 즐겨찾기
        self.main()

    def _getTitle(self, op1) :
        if op1 == "correct" :
            return "맞힌 단어장"
        elif op1 == "wrong" :
            return "틀린 단어장"
        else :
            print("AfterTestWordNote op1, op2 Error")
    
    def use_goBack(self) :
        if self._op2 == "review" :
            Goto.gotoReviewTestResult(self.user, self._wordIdxList, self._anotherList)
        elif self._op2 == "wrong" :
            Goto.gotoWrongNoteTestResult(self.user, self._wordIdxList, self._anotherList)
        elif self._op2 == "bookmark" :
            Goto.gotoBookmarkNoteTestResult(self.user, self._wordIdxList, self._anotherList)
        elif self._op2 == "entire" :
            Goto.gotoEntireTestResult(self.user, self._wordIdxList, self._anotherList)
        else :
            print("op2 error")


    def use_gotoSelectTest(self) :
        Goto.gotoHome(self.user)

