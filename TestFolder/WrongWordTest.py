import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from uitest.WrongWordTestUI import MainWindow
from Test import Test
from Goto import Goto
import random


class WrongWordTest(Test) :        
    def main(self) :
        self.window = MainWindow(self)
        self.window.show()

    def select_random_20(numbers):
        result = numbers
        if len(numbers) > 20:
            result = random.sample(numbers, 20)
        return result
    
    def _reflectCorrect(self) : #맞았을 때, 오답노트에서 삭제 
        self._correctCount += 1
        self._correctIdxList.append(self._wordIdxList[self._wordCount])
        self.db.DeleteWrongWordIdxList(self.user, self._wordIdxList[self._wordCount])
    
    def _setTitle(self) :
        return "오답노트 테스트"
    
    def use_goBack(self) :
        Goto.gotoWrongWordNote(self.user)

    def use_gotoSelectTestResult(self) :
        self._dbClose()
        Goto.gotoWrongNoteTestResult(self.user, self._correctIdxList, self._wrongIdxList)