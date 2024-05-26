from WordNote import WordNote
from Goto import Goto

class ReviewWordNote(WordNote) : # WordNote를 상속받은 유닛 단어장 클래스(복습 테스트와 이름을 맞췄음)
    def __init__(self, part, unit) :
        self._titleName = self._getPartName(part)
        self._testName = "복습 테스트 시작"
        self._testChoice = False
        self._wordIdxList = self._makeWordIdxList(part, unit) # index로 구성된 리스트
        self.db = self._makeDBobj()
        self._wordList = self._returnWordList()
        self.main()
        
    def _getPartName(self, part) :
        partNum = part
        partName = "Part" + str(partNum)
        return partName

    def use_goBack(self) :
        self._dbClose()
        Goto.gotoUnit()
    
    def use_gotoSelectTest(self) :
        self._dbClose()
        Goto.gotoReviewTest(self._wordIdxList, self._testChoice)
        
    def _makeWordIdxList(self, part, unit) :
        idx = (part-1) * 150 + (unit-1) * 10
        idxList = []
        for i in range(1, 11) :
            idx += 1
            idxList.append(idx)
        print(idx)
        return idxList
    
    def use_gotoSelectTest(self) :
        Goto.gotoReviewTest(self._wordIdxList, self._testChoice)