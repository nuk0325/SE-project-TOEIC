import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from service.test_result import TestResult
from goto_service import Goto
from UI.test_result_ui import ReviewTestResultUI #DB 조작 유닛 테스트
from DB_manager import DBManager #DB 조작 추가

class ReviewTestResult(TestResult) :
    def __init__(self, user, correctWordIdxList, wrongWordIdxList) :
        super.__init__(user, correctWordIdxList, wrongWordIdxList)
        self.db = self._makeDBobj() #DB 조작 추가. 유닛 클리어에 대해 반영

    def main(self) :
        self.window = ReviewTestResultUI(self) #DB 조작 유닛 테스트
        self.window.show()
    
    def _makeDBobj(self) :
        return DBManager()

    def getTitle(self) :
        return "테스트 결과"

    def checkCorrectRate(self) : #100퍼센트 맞추면 1:100 비율 틀린:맞은
        if self._correctCount >= self._wrongCount * 0 :
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
    
    def _calculateUnit_idx(self) : #DB에 저장된 형태. 120개의 유닛인덱스 반환
        return self._calculateIdx()/15 - 1
    
    def use_goBack(self) :
        self.use_goBackSelectWordNote()

    def use_goBackSelectWordNote(self):
        part, unit = self._calculateUnit()
        Goto.gotoUnitWordNote(part, unit, self.user)

    def getOp2(self) :
        return "review"
    




    