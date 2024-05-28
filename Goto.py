

class Goto :
    def gotoHome() :
        pass
    
    def goMyPage() :
        pass



    def gotoReviewWordNote(user, part, unit) :
        from WordNoteFolder.ReviewWordNote import ReviewWordNote
        ReviewWordNote(user, part, unit)

    def gotoAfterTestWordNote(user, lst, anotherList, op1, op2) :
        from WordNoteFolder.AfterTestWordNote import AfterTestWordNote
        AfterTestWordNote(user, lst, anotherList, op1, op2)
    










    def gotoWrongTest(user, correctList, wrongList) :
        #from TestResultFolder.WrongNoteTest import WrongNoteTest
        #대충 생성자
        pass
    
    def gotoBookmarkNoteTest(wordList) :
        pass

    def gotoReviewTest(user, wordList, testChoice) :
        from TestFolder.ReviewTest import ReviewTest
        ReviewTest(user, wordList, testChoice)





    def gotoReviewTestResult(user, correctList, wrongList) :
        from TestResultFolder.ReviewTestResult import ReviewTestResult
        ReviewTestResult(user, correctList, wrongList)

    def gotoWrongNoteTestResult(user, correctList, wrongList) :
        pass

    def gotoBookmarkNoteTestResult(user, correctList, wrongList) :
        pass
    
    def gotoEntireTestResult(user, correctList, wrongList) :
        pass







    def gotoUnit() :
        pass