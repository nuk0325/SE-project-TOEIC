import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from TestResult import TestResult
from Goto import Goto
from uitest.TestResultUI import EntireTestResultUIMainWindow

class EntireTestResult(TestResult) :
    def main(self) :
        self.window = EntireTestResultUIMainWindow(self)
        self.window.show()

    def getTitle(self) :
        return "테스트 결과"
    
    def use_goBack(self) :
        self.use_goBackSelectWordNote()

    def use_goBackSelectWordNote(self):
        Goto.gotoPrepareEntireTest(self.user) # 전체 테스트 준비화면으로 가기

    def getOp2(self) :
        return "entire"