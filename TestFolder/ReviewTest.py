import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Test import Test
from Goto import Goto


class ReviewTest(Test) :        
    def _setTitle(self) :
        return "복습 테스트"
    

    def _calculateUnit(self) : # 인덱스를 근거로 Part와 Unit을 구하는 함수
        num = self._wordIdxList[0]
        part = num // 150 + 1
        unit = (num % 150) // 10 + 1
        return part, unit
    
    def getUnitNum(self) : # UI에 unit1 이런거 값 주는 함수
        unit = self._calculateUnit()[1]
        unitName = "unit" + str(unit)
        return unitName
    
    def use_goBack(self) :
        part, unit = self._calculateUnit()
        Goto.gotoReviewWordNote(self.user, part, unit)

    def use_gotoSelectTestResult(self) :
        self._dbClose()
        Goto.gotoReviewTestResult(self.user, self._correctIdxList, self._wrongIdxList)