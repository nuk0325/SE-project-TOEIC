from WordNote import WordNote
from Goto import Goto

class WrongNote(WordNote) :
    def __init__(self, recievedWordList) :
        self._titleName = "오답노트"
        self._wordList = recievedWordList
        for i in range(self._wordList) :
            self._wordMeanList.append(0)
            
    def use_goBack() :
        Goto.goMyPage()
        
    def use_gotoSelectTest(self):
        Goto.gotoWrongNoteTest(self._wordList)