from WordNote import WordNote
from Goto import Goto

class ReviewWordNote(WordNote) : # WordNote를 상속받은 유닛 단어장 클래스(복습 테스트와 이름을 맞췄음)
    def __init__(self, recievedWordList) :
        self._titleName = "학습하기"
        self._testName = "복습 테스트 시작"
        self._testChoice = False
        self._wordIdxList = recievedWordList # index로 구성된 리스트
        self.db = self._makeDBobj()
        self._wordList = self._returnWordList()

    def use_goBack() :
        Goto.gotoUnit()
    
    def use_gotoSelectTest(self) :
        Goto.gotoReviewTest(self._wordIdxList, self._testChoice)