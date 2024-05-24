from Test import Test

class ReviewTest(Test) :
    def _setTitle(self) :
        self._titleName = "복습 테스트"
    
    def getUnitNum(self) :
        max = 1200
        for word in self._wordList :
            if word < max :
                max = word
        if max == 0 : return 0
        unitInt =  int(word / len(self._wordList) + 1)
        unitName = "unit" + str(unitInt)
        return unitName