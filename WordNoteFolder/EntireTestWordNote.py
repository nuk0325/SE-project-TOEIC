from WordNote import WordNote
from Goto import Goto
import random

class EntireTestWordNote(WordNote) :
    def __init__(self,user, testChoice, word_n) :
        self.user = user
        self._titleName = ""
        self._testName = ""
        self._testChoice = testChoice # 단어 / 뜻 전환 여부 / False면 뜻으로 답하기
        self.word_n = int(word_n)
        self.db = self._makeDBobj()
        self._wordIdxList = self.db.getEntireTestWordList(self.user) # 모든 단어들의 인덱스리스트 가져오기
        self._wordList = self._returnWordList()
        self.main()

    def main(self) : # UI 실행안함. 바로 테스트 시작
        wordIdxList = self.select_random_n(self._wordIdxList, self.word_n)
        Goto.gotoEntireTest(self.user, wordIdxList, self._testChoice)

    def select_random_n(self, wordIdxList, word_n): # 전체 단어 1200개중에 n개의 단어를 뽑음
        result = random.sample(wordIdxList, word_n)
        return result
    
    def use_goBack(self) :
        self._dbClose()
        Goto.gotoMypage()
    
    def use_gotoSelectTest(self) :
        self._dbClose()
        Goto.gotoBookmarkNoteTest(self.user, self._wordIdxList, self._testChoice)
      