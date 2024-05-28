import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Goto import Goto
from uitest.TestResultUI import MainWindow

class TestResult :
    def __init__(self, user, correctWordIdxList, wrongWordIdxList) :
        self.user = user
        self.correctWordIdxList = correctWordIdxList
        self.wrongWordIdxList = wrongWordIdxList
        self.correctCount = len(correctWordIdxList)
        self.wrongCount = len(wrongWordIdxList)
        self.main()

    def main(self) :
        self.window = MainWindow(self)
        self.window.show()

    def _ifCorrectOver(self) :
        if self.correctCount >= self.wrongCount * 4 :
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
            lst = self.correctWordIdxList
            anotherList = self.wrongWordIdxList
        elif op1 == "wrong" :
            lst = self.wrongWordIdxList
            anotherList = self.correctWordIdxList
        else :
            print("error")
        Goto.gotoAfterTestWordNote(self.user, lst, anotherList, op1, self.getOp2())

    def use_goBackSelectWordNote(self) :
        pass

    def getCorrectCount(self) :
        return str(self.correctCount)
    
    def getWrongCount(self) :
        return str(self.wrongCount)
    
    def getOp2() : # Review인지 wrong인지 bookmark인지에 따라
        pass # 상속받아서 return (ex. return "wrong")