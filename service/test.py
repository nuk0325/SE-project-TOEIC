import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#from PyQt6.QtWidgets import QApplication
from UI.review_test_ui import ReviewTestUI
from DB_manager import DBManager
from goto_service import Goto
import random

class Test :  
    def __init__(self, user, receivedWordList, testChoice) :
        self.user = user
        self._titleName = self._setTitle()
        self._correctCount = 0
        self._wrongCount = 0
        self._wordCount = 0
        self._wordIdxList = []
        self._correctIdxList = []
        self._wrongIdxList = [] # 셋 전부 index의 배열
        self._wordIdxList = receivedWordList 
        self._shuffleWordIdxList()
        self._testChoice = testChoice # True면 영어로 답하기 / False면 뜻으로 답하기
        self._wrongMeaningList = self._makeWrongMeaningList()
        
        self.db = DBManager()
        self.goto = Goto()
        
        self.main()

    def main(self) :
        self.window = ReviewTestUI(self)
        self.window.show()

    def _setTitle(self) : # 상속해서 오버라이딩 될 메서드
        return ""
    
    def _shuffleWordIdxList(self) :
        random.shuffle(self._wordIdxList)

    def _reflectCorrect(self) : #맞았을 때, 오답노트에서 삭제 
        self._correctCount += 1
        self._correctIdxList.append(self._wordIdxList[self._wordCount])
    
    def _reflectWrong(self) : #틀렸을 때, 오답노트에 추가
        self._wrongCount += 1
        self._wrongIdxList.append(self._wordIdxList[self._wordCount])
        self.db.insertWrongWordIdxList(self.user, self._wordIdxList[self._wordCount])
    
    def _dbClose(self) :
        self.db.closeDB()

    def afterQuestion(self, answer) :
        if answer == self.getAnswer() :
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
        self.goto.gotoHome(self.user)

    def use_gotoSelectTestResult(self) :
        pass

    def getTitle(self) :
        return self._titleName
    
    def getQuestion(self) :
        idx = self._wordIdxList[self._wordCount]
        if self._testChoice :
            return self.db.getWord(idx, "meaning")
        else :
            return self.db.getWord(idx, "word")

    def getAnswer(self) :
        idx = self._wordIdxList[self._wordCount]
        if self._testChoice :
            return self.db.getWord(idx, "word")
        else :
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
        if self._testChoice :
            option = "word"
        else :
            option = "meaning"
        for idx in idxList :
            word = self.db.getWord(idx, option)
            wordList.append(word) # 뜻 str로 이루어진 리스트를 return한다
        return wordList
        
    def getCorrectCount(self) :
        return str(self._correctCount)
    
    def getWrongCount(self) :
        return str(self._wrongCount)