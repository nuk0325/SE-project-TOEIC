from word_note import WordNote
from goto_service import Goto

class AfterTestWordNote(WordNote) :
    def __init__(self, user, wordIdxList, anotherList, op1, op2) :
        self.user = user
        self._wordIdxList = wordIdxList
        self._anotherList = anotherList
        self._op1 = op1
        self._titleName = "테스트 결과"
        self._label = self._makeLabel()
        self._testName = "홈으로 가기"
        self.db = self._makeDBobj()
        self._wordList = self._returnWordList()
        self._op2 = op2 # 어디로 돌아가는지에 대한 옵션
        # review -> 복습 / wrong -> 오답 / fav -> 즐겨찾기
        self.main()

    def _makeLabel(self) :
        if self._op1 == "correct" :
            return "맞힌 단어"
        elif self._op1 == "wrong" :
            return "틀린 단어"
        else :
            print("AfterTestWordNote op1, op2 Error")

    def getLabel(self) :
        return self._label
    
    def use_goBack(self) :
        lst1 = self._wordIdxList
        lst2 = self._anotherList
        if self._op1 == "wrong" : # 틀린 단어장이면 wordIdxList와 anotherList의 파라미터 위치 바꾸기
            lst1, lst2 = self._reverseList(lst1, lst2) # 이유 : 틀린 단어장이면 wordIdxList가 틀린 단어 리스트인데,
                                                    # 원래대로 넣으면 틀린 단어가 맞은 단어 리스트의 파라미터로서 실행된다
        if self._op2 == "review" :
            Goto.gotoReviewTestResult(self.user, lst1, lst2)
        elif self._op2 == "wrong" :
            Goto.gotoWrongNoteTestResult(self.user, lst1, lst2)
        elif self._op2 == "bookmark" :
            Goto.gotoBookmarkNoteTestResult(self.user, lst1, lst2)
        elif self._op2 == "entire" :
            Goto.gotoEntireTestResult(self.user, lst1, lst2)
        else :
            print("op2 error")

    def _reverseList(self, lst1, lst2) :
        return lst2, lst1

    def use_gotoSelectTest(self) :
        self.goto.gotoHome(self.user)

