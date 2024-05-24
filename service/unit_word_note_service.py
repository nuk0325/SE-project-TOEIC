from PyQt6.QtWidgets import QMainWindow
from word_note import WordNote
from goto_service import Goto

class UnitWordNote(WordNote, QMainWindow) : # WordNote를 상속받은 유닛 단어장 클래스(복습 테스트와 이름을 맞췄음)
     def __init__(self, recievedWordList) :
        self._titleName = "학습하기"
        self._testName = "복습 테스트 시작"
        self._testChoice = False
        self._wordIdxList = recievedWordList # index로 구성된 리스트
        self.db = self._makeDBobj()
        self._wordList = self._returnWordList()

    def use_goBack(self) :
        # self.goto.gotoUserUnit()
        pass
    
    def use_gotoSelectTest(self) :
        # self.goto.gotoReviewTest(self._wordList, self._testChoice)
        pass