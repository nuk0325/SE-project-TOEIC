from word_note import WordNote
from goto_service import Goto

class UnitWordNote(WordNote) : # WordNote를 상속받은 유닛 단어장 클래스(복습 테스트와 이름을 맞췄음)
    def __init__(self, part, unit, user) :
        self._titleName = self._getPartName(part)
        self._testName = "복습 테스트 시작"
        self._testChoice = False
        self._wordIdxList = self._makeWordIdxList(part, unit) # index로 구성된 리스트
        self.db = self._makeDBobj()
        self._wordList = self._returnWordList()

        self.part = part
        self.user = user

        self.goto = Goto()
        self.main(self.user)
        
    def _getPartName(self, part) :
        partNum = part
        partName = "Part" + str(partNum)
        return partName

    def use_goBack(self) :
        self._dbClose()
        self.goto.gotoUserUnit(self.part, self.user)
    
    def use_gotoSelectTest(self) :
        self._dbClose()
        self.goto.gotoReviewTest(self._wordIdxList, self._testChoice)
        
    def _makeWordIdxList(self, part, unit) :
        idx = (part-1) * 120 + (unit-1) * 10
        idxList = []
        for i in range(1, 11) :
            idx += 1
            idxList.append(idx)
        print(idx)
        return idxList
    
    def use_gotoSelectTest(self) :
        Goto.gotoReviewTest(self._wordIdxList, False)