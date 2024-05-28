

class Goto :
    def gotoHome() :# 홈 화면으로 가기
        pass
    
    def goMyPage() :# 마이페이지 화면으로 가기
        pass



    def gotoReviewWordNote(user, part, unit) : #유닛 단어장으로 가기
        from WordNoteFolder.ReviewWordNote import ReviewWordNote
        ReviewWordNote(user, part, unit)

    def gotoWrongWordNote(user) : #오답노트 단어장으로 가기
        from WordNoteFolder.WrongWordNote import WrongWordNote
        WrongWordNote(user)

    def gotoBookmarkWordNote(user) : #즐겨찾기 단어장으로 가기
        from WordNoteFolder.BookmarkWordNote import BookmarkWordNote
        BookmarkWordNote(user)


    def gotoAfterTestWordNote(user, lst, anotherList, op1, op2) : #테스트 결과 단어장으로 가기. 맞춘단어 or 틀린단어
        from WordNoteFolder.AfterTestWordNote import AfterTestWordNote
        AfterTestWordNote(user, lst, anotherList, op1, op2)
    










    def gotoWrongTest(user, correctList, wrongList) : 
        #from TestResultFolder.WrongNoteTest import WrongNoteTest
        #대충 생성자
        pass
    
    def gotoWrongWordTest(user, wordList, testChoice) : #오답노트 테스트
        from TestFolder.WrongWordTest import WrongWordTest
        WrongWordTest(user, wordList, testChoice)
        pass

    def gotoBookmarkNoteTest(user, wordList, testChoice) : #즐겨찾기 테스트
        from TestFolder.BookmarkTest import BookmarkTest
        BookmarkTest(user, wordList, testChoice)
        pass

    def gotoReviewTest(user, wordList, testChoice) : # 유닛.복습 테스트
        from TestFolder.ReviewTest import ReviewTest
        ReviewTest(user, wordList, testChoice)

    def gotoEntireTest(user, wordList, testChoice) : #전체 테스트
        from TestFolder.EntireTest import EntireTest
        EntireTest(user, wordList, testChoice)
        pass





    def gotoReviewTestResult(user, correctList, wrongList) : #오답노트 테스트 결과로 가기
        from TestResultFolder.ReviewTestResult import ReviewTestResult
        ReviewTestResult(user, correctList, wrongList)

    def gotoWrongNoteTestResult(user, correctList, wrongList) : #즐겨찾기 테스트 결과로 가기
        from TestResultFolder.WrongWordTestResult import WrongWordTestResult
        WrongWordTestResult(user, correctList, wrongList)
        pass

    def gotoBookmarkNoteTestResult(user, correctList, wrongList) : # 유닛.복습 테스트 결과로 가기
        from TestResultFolder.BookmarkTestResult import BookmarkTestResult
        BookmarkTestResult(user, correctList, wrongList)
        pass
    
    def gotoEntireTestResult(user, correctList, wrongList) : #전체 테스트 결과로 가기
        from TestResultFolder.EntireTestResult import EntireTestResult
        EntireTestResult(user, correctList, wrongList)
        pass



    def gotoUnit() : # 유닛 단어장에서 뒤로가기 눌렀을 때
        pass
