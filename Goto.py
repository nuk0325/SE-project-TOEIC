

class Goto :
    def gotoHome() :
        pass
    
    def goMyPage() :
        pass

    def gotoReviewWordNote(user, part, unit) :
        from WordNoteFolder.ReviewWordNote import ReviewWordNote
        ReviewWordNote(user, part, unit)

    def gotoAfterTestWordNote(user, lst, anotherList, option) :
        from WordNoteFolder.AfterTestWordNote import AfterTestWordNote
        AfterTestWordNote(user, lst, anotherList, option)
    
    def gotoWrongNoteTest(wordlist) :
        pass
    
    def gotoBookmarkNoteTest(wordList) :
        pass

    def gotoReviewTestResult(user, correctList, wrongList) :
        from TestResultFolder.ReviewTestResult import ReviewTestResult
        ReviewTestResult(user, correctList, wrongList)

    def gotoReviewTest(self, wordList, testChoice) :
        from TestFolder.ReviewTest import ReviewTest
        ReviewTest(self, wordList, testChoice)

    def gotoUnit() :
        pass