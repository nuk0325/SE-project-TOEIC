from Test import Test
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class ReviewTest(Test) :
    def _setTitle(self) :
        return "복습 테스트"
    
    def getUnitNum(self) :
        max = 1200
        for word in self._wordList :
            if word < max :
                max = word
        if max == 0 : return 0
        unitInt =  int(word / len(self._wordList) + 1)
        unitName = "unit" + str(unitInt)
        return unitName