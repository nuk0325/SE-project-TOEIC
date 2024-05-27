import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from TestResult import TestResult
from Goto import Goto

class ReviewTestResult(TestResult) :

    def getTitle(self) :
        return "테스트 결과"

    def _calculateIdx(self) :
        min = 1200
        lst = self.correctWordIdxList + self.wrongWordIdxList
        for idx in lst :
            if min > idx :
                min = idx
        return min
    
    def _calculateUnit(self) :
        num = self._calculateIdx()
        part = num // 150 + 1
        unit = (num % 150) // 10 + 1
        return part, unit

    def goBackSelectWordNote(self):
        part, unit = self._calculateUnit()
        Goto.gotoReviewWordNote(self.user, part, unit)