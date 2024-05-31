#from DB.DBcontrol import DBcontrol

class Word :
    def __init__(self, user, idx, db) :
        self.user = user
        self.db = db
        self._idx = idx # 해당 단어의 인덱스
        self._wordName = self.db.getWord(idx, "word")
        self._meaning = self.db.getWord(idx, "meaning")
        self._sentence = self.db.getWord(idx, "sentence")
        self._sentMeaning = self.db.getWord(idx, "sentMeaning")
        
    def getBookmark(self) : # 해당 단어가 즐겨찾기에 해당하는지 아닌지 True or False로 return
        return self.db.checkBookmark(self.user, self._idx)
        
    def Bookmark(self) : # 즐겨찾기 등록 / 삭제
        self.db.changeBookmark(self.user, self.getBookmark(), self._idx)
    
    def getWordIdx(self) :
        return self._idx

    def getWordName(self) :
        return self._wordName
    
    def getMeaning(self) :
        return self._meaning
    
    def getSentence(self) :
        return self._sentence
    
    def getSentMeaning(self) :
        return self._sentMeaning