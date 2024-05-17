import sys
sys.path.append('DB') # 아마 sevice같은거 import해서 거기다가 맡길 듯
import sqlite3
from Goto import Goto

class WordNote :
    _titleName = ""
    _wordList = []
    _wordMeanList = [] # 기존 wordMean을 리스트로 만든 것
    
    def __init__(self, recievedWordList) :
        self._wordList = recievedWordList
        for i in range(self._wordList) :
            self._wordMeanList.append(0)
        
    def addBookMark(wordId) :
        conn = sqlite3.connect('word.db')
        cur = conn.cursor()
        user_id = "hello world" # 받아오기
        is_right = cur.execute('''SELECT wro_fav SET fav_is_right WHERE user_id = ? AND line_num = ?, (user_id, wordId)''')
        if is_right == 1 :
            print("즐겨찾기 불 꺼지게 하기")
            cur.execute('''UPDATE wro_fav SET fav_is_right = 0 WHERE user_id = ? AND line_num = ?, (user_id, wordId)''')
        else :
            print("즐겨찾기 불 켜지게 하기")
            cur.execute('''UPDATE wro_fav SET fav_is_right = 1 WHERE user_id = ? AND line_num = ?, (user_id, wordId)''')
        
    
    def showWordMean(self, wordId) :
        if self._wordMeanList[wordId] == 0 :
            self._wordList[wordId] = 1
            # wordId번째 뜻 보기 열리게 하기? 
        else :
            self._wordList[wordId] = 0
            # wordId번째 뜻 보기 닫히게 하기?
    
    def showWordMeanAll(self) : # 전체 단어/뜻 보기
        for i in range(len(self._wordList)) :
            if self._wordMeanList[i] == 0 :
                self.showWordMean(i)
                
    def use_gotoHome() :
        Goto.gotoHome()
        
    def use_goBack() : # 뒤로가기 버튼은 자식이 오버라이딩해서 구현하게 할 예정
        pass
    
    def use_gotoSelectTest() :
        pass