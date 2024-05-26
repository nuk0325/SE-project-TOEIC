import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from PyQt6.QtWidgets import QApplication
from goto_service import Goto
from Word import Word
from WordNoteUI import MainWindow
from DBcontrol import DBcontrol
        
class WordNote :    
    def __init__(self, recievedWordList) :
        self._titleName = "" # 맨 위에 들어가는 문장 (ex. 학습하기)
        self._testName = "" # 맨 아래에 들어가는 문장 (ex. 복습 테스트 시작)
        self._testChoice = False # 단어 / 뜻 전환 여부 (아직 구현 안 됨)
        self._wordIdxList = recievedWordList # 단어들의index로 구성된 리스트
        self.db = self._makeDBobj()
        self._wordList = self._returnWordList() # word 객체로 구성된 리스트
        self.main()

    def _makeDBobj(self) :
        return DBcontrol()

    def _returnWordList(self) : # word 객체 리스트 만드는 함수
        lst = []
        for idx in self._wordIdxList :  
            word = Word(idx, self.db) 
            lst.append(word)
        return lst

    def main(self) : # UI 실행 함수
        frameCount = len(self._wordIdxList)
        noteLabel = self._titleName
        testName = self._testName
        wordObjList = self._wordList
        app = QApplication(sys.argv)
        self.window = MainWindow(frameCount, noteLabel, testName, wordObjList, self)
        self.window.show()
        sys.exit(app.exec())

    def _dbClose(self) :
        # self.db.closeDB()
        pass
                
    def use_gotoHome(self) : # 홈으로 가기 버튼
        self._dbClose() # 다른 페이지로 가기 전에 db.close() 잊지 말기 (여러개가 열려있으면 충돌남)
        Goto.gotoHome()
        
    def use_goBack() : # 뒤로가기 버튼은 자식이 오버라이딩해서 구현하게 할 예정
        pass
    
    def use_gotoSelectTest() : # 얘도 자식이 오버라이딩
        pass

#if __name__ == "__main__": # 실제 UI 실행 코드
#    received_word_list = []  # 받은 단어 목록을 입력하세요.
#    word_note = WordNote(received_word_list)
#    word_note.main()