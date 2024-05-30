import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from goto_service import Goto
from UI.test_result_ui import TestResultUI

class TestResult :
    def __init__(self, user, correctWordIdxList, wrongWordIdxList) :
        self.user = user
        self._correctWordIdxList = correctWordIdxList
        self._wrongWordIdxList = wrongWordIdxList
        self._correctCount = len(correctWordIdxList)
        self._wrongCount = len(wrongWordIdxList)
        self.main()

        self.goto = Goto()

    def main(self) :
        self.window = TestResultUI(self)
        self.window.show()

    def checkCorrectRate(self) : #80퍼센트 이사 맞추면 1:4 비율 틀린:맞은
        if self._correctCount >= self._wrongCount * 4 :
            return True
        else :
            return False

    def getColor(self) :
        str = "background-color : "
        if self.checkCorrectRate() :
            color = "#8bdbad ;"
        else :
            color = "#739bc3 ;"
        return str + color
    
    def getResultSentence(self) :
        if self.checkCorrectRate() :
            return "너무 잘했어요!"
        else :
            return "조금 더 노력해봐요!"
    
    def use_goBack(self) :
        pass

    def use_gotoHome(self) :
        self.goto.gotoHome(self.user)

    def use_gotoAfterTestWordNote(self, op1) :
        if op1 == "correct" :
            lst = self._correctWordIdxList
            anotherList = self._wrongWordIdxList
        elif op1 == "wrong" :
            lst = self._wrongWordIdxList
            anotherList = self._correctWordIdxList
        else :
            print("error")
        self.goto.gotoAfterTestWordNote(self.user, lst, anotherList, op1, self.getOp2())

    def use_goBackSelectWordNote(self) :
        pass

    def getCorrectCount(self) :
        return str(self._correctCount)
    
    def getWrongCount(self) :
        return str(self._wrongCount)
    
    def getOp2() : # Review인지 wrong인지 bookmark인지에 따라
        pass # 상속받아서 return (ex. return "wrong")