import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Goto import Goto
from uitest.TestResultUI import MainWindow

class TestResult :
    def __init__(self, user, correctWordIdxList, wrongWordIdxList) :
        self.user = user
        self._correctWordIdxList = correctWordIdxList
        self._wrongWordIdxList = wrongWordIdxList
        self._correctCount = len(correctWordIdxList)
        self._wrongCount = len(wrongWordIdxList)
        self.main()

    def main(self) :
        self.window = MainWindow(self)
        self.window.show()

    def _ifCorrectOver(self) : # 맞은 개수가 80%를 넘었으면
        if self._correctCount >= self._wrongCount * 4 :
            return True
        else :
            return False

    def getColor(self) :
        str = "background-color : "
        if self._ifCorrectOver() :
            color = "#8bdbad ;"
        else :
            color = "#739bc3 ;"
        return str + color
    
    def use_goBack(self) :
        pass

    def use_gotoHome(self) :
        Goto.gotoHome()

    def use_gotoAfterTestWordNote(self, op1) :
        if op1 == "correct" :
            lst = self._correctWordIdxList
            anotherList = self._wrongWordIdxList
        elif op1 == "wrong" :
            lst = self._wrongWordIdxList
            anotherList = self._correctWordIdxList
        else :
            print("error")
        Goto.gotoAfterTestWordNote(self.user, lst, anotherList, op1, self.getOp2())

    def use_goBackSelectWordNote(self) :
        pass

    def getCorrectCount(self) :
        return str(self._correctCount)
    
    def getWrongCount(self) :
        return str(self._wrongCount)
    
    def getOp2() : # Review인지 wrong인지 bookmark인지에 따라
        pass # 상속받아서 return (ex. return "wrong")