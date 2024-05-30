import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from UI.wrong_note_test_ui import WrongNoteTestUI
from service.test import Test
from goto_service import Goto
import random


class WrongNoteTest(Test) :        
    def main(self) :
        self._wordIdxList=self.select_random_20(self._wordIdxList)
        self.window = WrongNoteTestUI(self)
        self.window.show()

    def select_random_20(self, wordIdxList):
        result = wordIdxList
        if len(wordIdxList) > 20:
            result = random.sample(wordIdxList, 20)
        return result
    
    def _reflectCorrect(self) : #맞았을 때, 오답노트에서 삭제 
        self._correctCount += 1
        self._correctIdxList.append(self._wordIdxList[self._wordCount])
        self.db.deleteWrongWordIdxList(self.user, self._wordIdxList[self._wordCount])
    
    def _setTitle(self) :
        return "오답노트 테스트"
    
    def use_goBack(self) :
        self.goto.gotoWrongNote(self.user)

    def use_gotoSelectTestResult(self) :
        self._dbClose()
        self.goto.gotoWrongNoteTestResult(self.user, self._correctIdxList, self._wrongIdxList)