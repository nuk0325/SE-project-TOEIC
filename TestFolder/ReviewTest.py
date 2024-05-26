import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Test import Test


class ReviewTest(Test) :        
    def _setTitle(self) :
        return "복습 테스트"
    
    
    def getUnitNum(self) :
        num = self._wordIdxList[0] % 150
        unit = 1
        while num > 10 :
            num -= 10
            unit += 1
        unitName = "unit" + str(unit)
        return unitName