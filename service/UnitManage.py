import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from WordForManager import WordForManager
from UI.ManagerUnitWordNoteUI import MainWindow
from service.DB_manager import DBManager
from service.goto_service import Goto

class UnitManage() :
    def __init__(self, user, part, unit) :
        self.user = user
        self._unitName = self._makeUnitName(part, unit)
        self._wordIdxList = self._makeWordIdxList(part, unit)
        self.db = self._makeDBobj()
        self._wordList = self._makeWordList()
        self._firstIdx = 0 # 단어 추가에 필요한 index
        self.main()

    def _makeWordIdxList(self, part, unit) :
        idx = (part-1) * 150 + (unit-1) * 10
        idxList = []
        for i in range(1, 11) :
            idx += 1
            idxList.append(idx)
        return idxList

    def _makeWordList(self) : # word 객체 리스트 만드는 함수
        lst = []
        for idx in self._wordIdxList :
            word = WordForManager(self.user, idx, self.db) 
            lst.append(word)
        return lst
    
    def _makeDBobj(self) :
        return DBManager()
    
    def main(self) :
        self.window = MainWindow(self)
        self.window.show()

    def getWordList(self) :
        return self._wordList
    
    def _makeUnitName(self, part, unit) :
        partName = "Part" + ' ' + str(part)
        unitName = "Unit " + ' ' + str(unit)
        name = partName + ' ' + '/' + ' '+ unitName
        return name
    
    def getUnitName(self) :
        return self._unitName
    
    def searchAndAdd(self) :
        for word in self._wordList :
            if word.getWordName() == None :
                self._firstIdx = word.getWordIdx()
                return 1
        return 0 # 유닛이 꽉 차 있을 경우
    
    def goAdd(self) :
        Goto.gotoManagerAddWord(self._firstIdx) 