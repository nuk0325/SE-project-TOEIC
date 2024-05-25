import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from PyQt6.QtWidgets import QApplication
from uitest.ReviewTestUI import MainWindow
from DB.DBcontrol import DBcontrol
from Goto import Goto
import random
#import time

class Test :  
    def __init__(self, recivedWordList, testChoice) :
        self._titleName = self._setTitle()
        self._correctCount = 0
        self._wrongCount = 0
        self._wordCount = 1
        self._wordList = []
        self._correctWordList = []
        self._wrongWordList = [] # 셋 전부 index의 배열
        self._wordList = recivedWordList
        self._testChoice = testChoice
        self._wrongWordList = self._makeWrongWordList()
        self.db = DBcontrol()
        print(self._titleName)
        self.main()

    def main(self) :
        #app = QApplication(sys.argv)
        self.window = MainWindow(self)
        self.window.show()
        #sys.exit(app.exec())
        
    def _setTitle(self) : # 상속해서 오버라이딩 될 메서드
        return ""
    
    def _reflectCorrect(self) :
        self._correctCount += 1
        self._correctWordList.append(self._wordCount)
    
    def _reflectWrong(self) :
        self._wrongCount += 1
        self._wrongWordList.append(self._wordCount)
    
    def _dbClose(self) :
        self.db.closeDB()

    def afterQuestion(self, answer) :
        if answer == self.getMeaning() :
            self._reflectCorrect()
        else :
            self._reflectWrong()
        self._wordCount += 1
        #time.sleep(3)
        if self._wordCount > len(self._wordList) :
            Goto.gotoTestResult(self._correctWordList, self._wrongWordList)

    def _makeWrongWordList(self) :
        num = len(self._wordList) * 3
        excluded_numbers = set(self._wordList)
        # wordList에 없는 숫자들 중에서 무작위로 샘플링된 숫자들의 리스트 생성
        lst = random.sample([x for x in range(1, 1201) if x not in excluded_numbers], num) # 1201은 나중에 바꿀 것
        return lst

    def getTitle(self) :
        return self._titleName
    
    def getWordName(self) :
        return self.db.getWord(self._wordCount, "word")

    def getMeaning(self) :
        meaning = self.db.getWord(self._wordCount, "meaning")
        print(meaning)
        return self.db.getWord(self._wordCount, "meaning")

    def getSentence(self) :
        return self.db.getWord(self._wordCount, "sentence")
    
    def getWordCountLabel(self) :
        wordCountStr = str(self._wordCount + 1)
        labelStr = wordCountStr + "번"
        return labelStr
    
    def getMeaningList(self) :
        idxList = []
        wordList = []
        idxList.append(self._wordCount)
        for _ in range(3) :
            idxList.append(self._wrongWordList.pop(0))
        random.shuffle(idxList)
        for idx in idxList :
            word = self.db.getWord(idx, "meaning")
            wordList.append(word)
        return wordList
        
    def getCorrectCount(self) :
        return str(self._correctCount)
    
    def getWrongCount(self) :
        return str(self._wrongCount)