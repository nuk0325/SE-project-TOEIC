from service.word_note import WordNote
from goto_service import Goto
from UI.word_note_ui import BookmarkNoteUI

class BookmarkNote(WordNote) :
    def __init__(self, user) :
        self.user = user
        self._titleName = "즐겨찾기"
        self._testName = "즐겨찾기 테스트 시작"
        self._testChoice = False
        self.db = self._makeDBobj()
        self._wordIdxList = self.db.getBookmarkWordList(self.user) # 즐겨찾기 단어들의 인덱스리스트 가져오기
        self._wordList = self._returnWordList()
        
        self.main()

        self.goto = Goto()

    def main(self) : # UI 실행 함수
        frameCount = len(self._wordIdxList)
        noteLabel = self._titleName
        testName = self._testName
        wordObjList = self._wordList
        #app = QApplication(sys.argv)
        self.window = BookmarkNoteUI(frameCount, noteLabel, testName, wordObjList, self) #WordNoteUI.py를 기반을 화면 구성
        self.window.show()
        #sys.exit(app.exec())
    
    def wordNoteCloseAndOpen(self): # 단어장 껐다가 키는. 단어 초기화하는 함수. 즐겨찾기에 사용
        #self._dbClose() #db닫기
        self.db = self._makeDBobj() #db열기
        self._wordIdxList = self.db.getBookmarkWordList(self.user) # 즐겨찾기 단어들의 인덱스리스트 가져오기
        self._wordList = self._returnWordList() # word 객체로 구성된 리스트
        self.main() # 단어장 UI 다시실행

    def use_goBack(self) :
        self._dbClose()
        self.goto.gotoMyPage(self.user)
    
    def use_gotoSelectTest(self) :
        self._dbClose()
        self.goto.gotoBookmarkNoteTest(self.user, self._wordIdxList, self._testChoice)
      