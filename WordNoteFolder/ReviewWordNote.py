from WordNote import WordNote
from Goto import Goto

class ReviewWordNote(WordNote) : # WordNote를 상속받은 유닛 단어장 클래스(복습 테스트와 이름을 맞췄음)
    def __init__(self, unit, part) :
        self._titleName = "학습하기"
        self._testName = "복습 테스트 시작"
        self._testChoice = False
        self._wordIdxList = self._makeWordIdxList(unit, part) # index로 구성된 리스트
        self.db = self._makeDBobj()
        self._wordList = self._returnWordList()
        self.main()

    def use_goBack(self) :
        self._dbClose()
        Goto.gotoUnit()
    
    def use_gotoSelectTest(self) :
        self._dbClose()
        Goto.gotoReviewTest(self._wordIdxList, self._testChoice)
        
    def _makeWordIdxList(self, unit, part) :
        idx = (unit-1) * 15
        idx = idx * (part-1) * 8
        idxList = []
        for i in range(1, 11) :
            idx += 1
            idxList.append(idx)
        return idxList