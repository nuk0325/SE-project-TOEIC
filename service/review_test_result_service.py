import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from test_result import TestResult
from goto_service import Goto

class ReviewTestResult(TestResult) :

    def getTitle(self) :
        return "테스트 결과"

    def checkCorrectRate(self) : #100퍼센트 맞추면 1:100 비율 틀린:맞은
        if self._correctCount >= self._wrongCount * 100 :
            return True
        else :
            return False
        
    def _calculateIdx(self) :
        min = 1200
        lst = self._correctWordIdxList + self._wrongWordIdxList
        for idx in lst :
            if min > idx :
                min = idx
        return min
    
    def _calculateUnit(self) :
        num = self._calculateIdx()
        part = num // 150 + 1
        unit = (num % 150) // 10 + 1
        return part, unit
    
    def use_goBack(self) :
        self.use_goBackSelectWordNote()

    def use_goBackSelectWordNote(self):
        part, unit = self._calculateUnit()
        self.goto.gotoUnitWordNote(self.user, part, unit)

    def getOp2(self) :
        return "review"