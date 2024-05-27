

class Goto :
    def gotoHome() :
        pass
    
    def goMyPage() :
        pass

    def gotoReviewWordNote(user, part, unit) :
        from WordNoteFolder.ReviewWordNote import ReviewWordNote
        ReviewWordNote(user, part, unit)
    
    def gotoWrongNoteTest(wordlist) :
        pass
    
    def gotoBookmarkNoteTest(wordList) :
        pass

    def gotoReviewTestResult(user, correctList, wrongList) :
        #from TestResultFolder.TestResult import TestResult
        #TestResult(user, correctList, wrongList)
        pass

    def gotoReviewTest(self, wordList, testChoice) :
        from TestFolder.ReviewTest import ReviewTest
        ReviewTest(self, wordList, testChoice)

    def gotoUnit() :
        pass