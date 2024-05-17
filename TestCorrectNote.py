from WordNote import WordNote
from Goto import Goto

class BookmarkNote(WordNote) :
    def __init__(self, recievedWordNote) :
        self._titleName = "테스트 결과"
        self._wordList = recievedWordNote
        for i in range(self._wordList) :
            self._wordMeanList.append(0)
            
        def use_goBack() :
            Goto.goMyPage()
            
        def use_gotoSelectPage(self) :
            Goto.gotoBookmarkNoteTest(self._wordList)