# from DB_manager import DBManager

class Word :
    def __init__(self, idx, db) :
        self.db = db
        self._idx = idx # 해당 단어의 인덱스
        self._wordName = self.db.getWord(idx, "word")
        self._meaning = self.db.getWord(idx, "meaning")
        self._sentence = self.db.getWord(idx, "sentence")
        
    def getBookmark(self) : # 해당 단어가 즐겨찾기에 해당하는지 아닌지 True or False로 return
        return self.db.checkBookmark(self._idx)
        
    def Bookmark(self) : # 즐겨찾기 등록 / 삭제
        self.db.changeBookmark(self.getBookmark(), self._idx)

    def getWordName(self) :
        return self._wordName
    
    def getMeaning(self) :
        return self._meaning
    
    def getSentence(self) :
        return self._sentence
    

    #추가
    @property
    def wordName(self):
        return self._wordName

    @wordName.setter
    def wordName(self, value):
        self._wordName = value

    @property
    def meaning(self):
        return self._meaning

    @meaning.setter
    def meaning(self, value):
        self._meaning = value

    @property
    def sentence(self):
        return self._sentence

    @sentence.setter
    def sentence(self, value):
        self._sentence = value