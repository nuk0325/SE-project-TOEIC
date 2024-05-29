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
        Goto.gotoPrepareEntireTest(self.user) #뒤로가기. 테스트준비화면으로

    def use_gotoSelectTestResult(self) : # 맞춘,틀린단어장에서 결과화면으로 돌아올 때
        self._dbClose()
        Goto.gotoEntireTestResult(self.user, self._correctIdxList, self._wrongIdxList) 