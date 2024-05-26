

class Goto :
    def gotoHome() :
        pass
    
    def goMyPage() :
        pass

    def gotoReviewWordNote(part, unit) :
        from WordNoteFolder.ReviewWordNote import ReviewWordNote
        ReviewWordNote(part, unit)
    
    def gotoWrongNoteTest(wordlist) :
        pass
    
    def gotoBookmarkNoteTest(wordList) :
        pass

    def gotoTestResult(correctList, wrongList) :
        #from TestResultFolder.TestResult import TestResult
        #TestResult(correctList, wrongList)
        pass

    def gotoReviewTest(wordList, testChoice) :
        from TestFolder.ReviewTest import ReviewTest
        ReviewTest(wordList, testChoice)

    def gotoUnit() :
        pass