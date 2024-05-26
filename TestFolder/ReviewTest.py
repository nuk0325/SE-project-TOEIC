import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from Test import Test
from Goto import Goto


class ReviewTest(Test) :        
    def _setTitle(self) :
        return "복습 테스트"
    
    
    def getUnitNum(self, option) :
        num = self._wordIdxList[0]
        part = num // 150 + 1
        unit = (num % 150) // 10 + 1

        if option == "partUnit" :
            return part, unit
        elif option == "unitName" :
            unitName = "unit" + str(unit)
            return unitName
        else :
            print("입력 오류")
    
    def use_goBack(self) :
        part, unit = self.getUnitNum("partUnit")
        Goto.gotoReviewWordNote(part, unit)