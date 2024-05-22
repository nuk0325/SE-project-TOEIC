from DB.DBcontrol import DBcontrol

class Word :
    def __init__(self, idx) :
        self.db = DBcontrol() # db : 데이터베이스를 총괄하는 객체
        self._idx = idx # 해당 단어의 인덱스
        self._wordName = self.db.getWord(idx, "word")
        self._meaning = self.db.getWord(idx, "meaning")
        self._sentence = self.db.getWord(idx, "sentence")
        
    def getBookmark(self) : # 해당 단어가 즐겨찾기에 해당하는지 아닌지 True or False로 return
        return self.db.checkBookmark(self._idx)
        
    def Bookmark(self) : # 즐겨찾기 등록 / 삭제
        self.db.changeBookmark(self.getBookmark())

    def getWordName(self) :
        return self._wordName
    
    def getMeaning(self) :
        return self._meaning
    
    def getSentence(self) :
        return self._sentence