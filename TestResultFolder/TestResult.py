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
    

    def use_goBack(self) :
        pass

    def use_gotoHome(self) :
        pass

    def use_gotoAfterTestWordNote(self, option) :
        if option == "correct" :
            lst = self.correctWordIdxList
        elif option == "wrong" :
            lst = self.wrongWordIdxList
        else :
            print("error")
        Goto.gotoAfterTestWordNote(self.user, lst, option)

    def goBackSelectWordNote(self) :
        pass


    def getCorrectCount(self) :
        return str(self.correctCount)
    
    def getWrongCount(self) :
        return str(self.wrongCount)