import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from uitest.BookmarkTestUI import MainWindow
from Test import Test
from Goto import Goto
import random


class BookmarkTest(Test) :        
    def main(self) :
        self._wordIdxList=self.select_random_20(self._wordIdxList)
        self.window = MainWindow(self)
        self.window.show()

    def select_random_20(self, wordIdxList):
        result = wordIdxList
        if len(wordIdxList) > 20:
            result = random.sample(wordIdxList, 20)
        return result
    
    def _setTitle(self) :
        return "즐겨찾기 테스트"
    
    def use_goBack(self) :
        Goto.gotoBookmarkWordNote(self.user)

    def use_gotoSelectTestResult(self) :
        self._dbClose()
        Goto.gotoBookmarkNoteTestResult(self.user, self._correctIdxList, self._wrongIdxList)