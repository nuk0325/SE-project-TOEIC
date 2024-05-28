import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from uitest.ReviewTestUI import MainWindow
from DB.DBcontrol import DBcontrol
from Goto import Goto
import random

class Test :  
    def __init__(self, user, recivedWordList, testChoice) :
        self.user = user
        self._titleName = self._setTitle()
        self._correctCount = 0
        self._wrongCount = 0
        self._wordCount = 0
        self._wordIdxList = []
        self._correctIdxList = []
        self._wrongIdxList = [] # 셋 전부 index의 배열
        self._wordIdxList = recivedWordList
        self._shuffleWordIdxList()
        self._testChoice = testChoice
        self._wrongMeaningList = self._makeWrongMeaningList()
        self.db = DBcontrol()
        self.main()

    def main(self) :
        self.window = MainWindow(self)
        self.window.show()
        
    def _setTitle(self) : # 상속해서 오버라이딩 될 메서드
        return ""
    
    def _shuffleWordIdxList(self) :
        random.shuffle(self._wordIdxList)
    
    def _reflectCorrect(self) :
        self._correctCount += 1
        self._correctIdxList.append(self._wordIdxList[self._wordCount])
    
    def _reflectWrong(self) :
        self._wrongCount += 1
        self._wrongIdxList.append(self._wordIdxList[self._wordCount])
        self.db.insertWrongWordIdxList(self.user, self._wordIdxList[self._wordCount])
    
    def _dbClose(self) :
        self.db.closeDB()

    def afterQuestion(self, answer) :
        if answer == self.getMeaning() :
            self._reflectCorrect()
        else :
            self._reflectWrong()
        self._wordCount += 1
        if self._wordCount == len(self._wordIdxList) :
            return False
        return True

    def _makeWrongMeaningList(self) :
        num = len(self._wordIdxList) * 3
        excluded_numbers = set(self._wordIdxList)
        # wordList에 없는 숫자들 중에서 무작위로 샘플링된 숫자들의 리스트 생성
        lst = random.sample([x for x in range(1, 1201) if x not in excluded_numbers], num) # 1201은 나중에 바꿀 것
        return lst
    
    def use_goBack(self) :
        pass
    
    def use_gotoHome(self) :
        Goto.gotoHome(self.user)

    def use_gotoSelectTestResult(self) :
        pass

    def getTitle(self) :
        return self._titleName
    
    def getWordName(self) :
        idx = self._wordIdxList[self._wordCount]
        return self.db.getWord(idx, "word")

    def getMeaning(self) :
        idx = self._wordIdxList[self._wordCount]
        return self.db.getWord(idx, "meaning")

    def getSentence(self) :
        idx = self._wordIdxList[self._wordCount]
        return self.db.getWord(idx, "sentence")
    
    def getWordCountLabel(self) :
        wordCountStr = str(self._wordCount+1)
        labelStr = wordCountStr + "번"
        return labelStr
    
    def getMeaningList(self) :
        idxList = []
        wordList = []
        idxList.append(self._wordIdxList[self._wordCount])
        for _ in range(3) :
            idxList.append(self._wrongMeaningList.pop()) # 정답 인덱스 하나에 오답 인덱스 3개
        random.shuffle(idxList) # 랜덤으로 섞기
        for idx in idxList :
            word = self.db.getWord(idx, "meaning")
            wordList.append(word) # 뜻 str로 이루어진 리스트를 return한다
        return wordList
        
    def getCorrectCount(self) :
        return str(self._correctCount)
    
    def getWrongCount(self) :
        return str(self._wrongCount)