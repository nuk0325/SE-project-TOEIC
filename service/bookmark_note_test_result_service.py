import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from test_result import TestResult

class BookmarkTestResult(TestResult) :

    def getTitle(self) :
        return "테스트 결과"
    
    def use_goBack(self) :
        self.use_goBackSelectWordNote()

    def use_goBackSelectWordNote(self):
        self.goto.gotoBookmarkNote(self.user)

    def getOp2(self) :
        return "bookmark"