from PyQt6.QtWidgets import QMainWindow
from word_note import WordNote
from goto_service import Goto

class UnitWordNote(WordNote, QMainWindow) : # WordNote를 상속받은 유닛 단어장 클래스(복습 테스트와 이름을 맞췄음)
    def __init__(self, user, part, unit) :
        self.user = user
        self._titleName = self._getPartName(part)
        self._label = self._makeLabel()
        self._testName = "복습 테스트 시작"
        self._testChoice = False
        self._wordIdxList = self._makeWordIdxList(part, unit) # index로 구성된 리스트
        self.db = self._makeDBobj()
        self._wordList = self._returnWordList()

        self.main()

        self.part = part
        self.goto = Goto()

    def _getPartName(self, part) :
        partNum = part
        partName = "Part" + str(partNum)
        return partName

    def _makeWordIdxList(self, part, unit) :
        idx = (part-1) * 150 + (unit-1) * 10
        idxList = []
        for i in range(1, 11) :
            idx += 1
            idxList.append(idx)
        return idxList

    def use_goBack(self) :
        self._dbClose()
        self.goto.gotoUserUnit(self.part, self.user)
    
    def use_gotoSelectTest(self) :
        self._dbClose()
        self.goto.gotoReviewTest(self.user, self._wordIdxList, self._testChoice)