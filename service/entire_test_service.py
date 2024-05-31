import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from UI.entire_test_ui import EntireTestUI
from service.test import Test
from goto_service import Goto


class EntireTest(Test) :        
    def main(self) :
        self.window = EntireTestUI(self)
        self.window.show()    
    
    def _setTitle(self) :
        return "전체 테스트"
    
    def use_goBack(self) :
        self.goto.gotoHome(self.user)

    def use_gotoSelectTestResult(self) :
        self._dbClose()
        self.goto.gotoEntireTestResult(self.user, self._correctIdxList, self._wrongIdxList)