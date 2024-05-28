import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from uitest.EntireTestTestUI import MainWindow
from Test import Test
from Goto import Goto


class EntireTest(Test) :        
    def main(self) :
        self.window = MainWindow(self)
        self.window.show()    
    
    def _setTitle(self) :
        return "전체 테스트"
    
    def use_goBack(self) :
        Goto.gotoBookmarkWordNote(self.user)

    def use_gotoSelectTestResult(self) :
        self._dbClose()
        Goto.gotoEntireTestResult(self.user, self._correctIdxList, self._wrongIdxList)