from PIL import Image

class TestResult :
    _correctCount = 0
    _wrongCount = 0
    _correctWordList = []
    _wrongWordList = []
    
    def __init__(self) :
        pass
    
    def printCorrectNum(self) : # --> getCorrectNum으로?
        return self.correctNum # 간단히 맞춘 개수를 리턴해서 그 값을 그대로 쓰면 된다
    
    def printWrongNum(self) :
        return self.wrongNum
    
    def printResultImage(self) :
        # image = Image.open("~~~.jpg")
        # 이미지 넘기기
        pass
    
    def gotoCorrectWordNote(self) :
        # WordNote.__init__(self, _correctWordList)
        pass
        
    def gotoWrongWordNote(self) :
        # WordNote.__init__(self, WrongWordList)
        pass
        
    def gotoHome() :
        # Home.__init__(self)
        # 그냥 인터페이스로 받을 홈으로 가기 함수를 이거 대신 해당 버튼에 박아도 되지 않을까
        pass
    
    def gotoSpecificPage() : #상속받아서 쓸 메서드
        # ex) WrongNote.__init__(self)
        pass