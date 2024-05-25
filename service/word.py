from DB_manager import DBManager

class Word:
    def __init__(self, idx) :
        self.data_manager = DBManager
        self._idx = idx # 해당 단어의 인덱스

        self._wordName = self.data_manager.getWord(idx, "word")
        self._meaning = self.data_manager.getWord(idx, "meaning")
        self._sentence = self.data_manager.getWord(idx, "sentence")
        
    def getBookmark(self) : # 해당 단어가 즐겨찾기에 해당하는지 아닌지 True or False로 return
        return self.data_manager.checkBookmark(self._idx)
        
    def Bookmark(self) : # 즐겨찾기 등록 / 삭제
        self.data_manager.changeBookmark(self.getBookmark(), self._idx)

    def getWordName(self) :
        return self._wordName
    
    def getMeaning(self) :
        return self._meaning
    
    def getSentence(self) :
        return self._sentence