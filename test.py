import random
import sys
sys.path.append('DB') # 아마 sevice같은거 import해서 거기다가 맡길 듯
import sqlite3
import time

class Test :
    _correctCount = 0 
    _wrongCount = 0
    _wordCount = 0 # wordList의 현재 인덱스를 가리킨다
    _wordList = []
    _correctWordList = []
    _wrongWordList = []
    # 이 리스트들은 전부 인덱스를 가지고 있는 int형 배열이라고 생각하면 된다
    
    def __init__(self) :
        # self._wordList = ~ 해서 _wordList 받아오기
        random.shuffle(self._wordList)
        self._wordCount = -1 #printQuestion을 실행하면 +1이 되어 0이 되니까
        self.printQuestion()
    
    
    def printQuestion(self) : # 문제마다 ui에 정보를 전달하는 함수
        self._wordCount += 1
        print(self.word[self._wordCount]) #실제로는 각 버튼 / label 마다 할당해줄 듯
                                        # 틀린 답 버튼에는 무슨 값을 넣어줘야할까(전체 단어장 랜덤? wordList에서 랜덤?)
        
        
    def printWordInformation(self) : # 문제 넘어가기 전에 뜻, 예문을 보여주는 함수
        conn = sqlite3.connect('word.db') #-----------여기부터
        cur = conn.cursor()
        mean, sent = cur.execute('''SELECT mean, sent FROM words_db WHERE line_num = ?''', (self._wordCount, )) #------- 여기까지 DB 건드는 클래스가 담당
        # 아마 service 쪽으로 뺼 지도
        print(mean, sent) # 각 칸에 할당 예정  ------------------ 이런건 UI 건드는 클래스가 담당
        time.sleep(3) # 3초 동안 보여주고 넘어감
        print("모든 버튼 색깔 정상적으로 돌리기(노란색, 회색)") #-------------- 이런 것도 UI에 연결해주는 클래스가 담당 (ex. UIdamdang_class.changeColor('button1','yellow'))
        self.printQuestion()
    
    def answerButtonAction(self, user_ans) : # user_ans는 string 타입으로 받으면 될 듯?
        conn = sqlite3.connect('word.db')
        cur = conn.cursor()
        real_ans = cur.execute('''SELECT mean FROM words_db WHERE line_num = ?''', (self._wordCount, ))
        if real_ans == user_ans :
            print("정답 파란색으로 바꾸기")
            self._correctCount += 1
            self._wordList.append(self._wordList[self._wordCount])
        else :
            print("해당 버튼 빨간색으로")
            print("정답 파란색으로 바꾸기")
            self._wrongCount += 1
            if user_ans != "정답보기" :
                self._wrongWordList.append(self._wordList[self._wordCount])
        self.printWordInformation()

