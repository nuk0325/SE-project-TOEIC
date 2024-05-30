'''
Goto Class
'''

class Goto():
    def gotoLogIn(self):
        print("go to Log-In Page")
        from log_in_service import LogIn
        self.window = LogIn()
        self.window.show()

    def gotoJoinMembership(self):
        print("go to Join Membership Page")
        from join_membership_service import JoinMembership
        self.window = JoinMembership()
        self.window.show()

    def gotoHome(self, user):
        print("go to Home")
        from home_service import Home
        self.window = Home(user)
        self.window.show()

    def gotoMyPage(self, user):
        print("go to My Page")
        from my_page_service import MyPage
        self.window = MyPage(user)
        self.window.show()

    def gotoUserPart(self, user):
        print("go to User Part Page")
        from user_part_service import UserPart
        self.window = UserPart(user)
        self.window.show()

    def gotoUserUnit(self, partNum, user):
        print("go to User Unit Page")
        from user_unit_service import UserUnit
        self.window = UserUnit(partNum, user)
        self.window.show()

    def gotoUnitWordNote(partNum, unitNum, user):
        print("go to Unit Word Note Page")
        from unit_word_note_service import UnitWordNote
        UnitWordNote(user, partNum, unitNum)

    def gotoReviewTest(self, user, wordIdxList, testChoice):
        print("go to Review Test Page")
        from review_test_service import ReviewTest
        ReviewTest(user, wordIdxList, testChoice)

    def gotoReviewTestResult(self, user, correctIdxList, wrongIdxList):
        print("go to Review Test Result Page")
        from review_test_result_service import ReviewTestResult
        ReviewTestResult(user, correctIdxList, wrongIdxList)

    def gotoPrepareEntireTest(self, user):
        print("go to Prepare Entire Test Page")
        from prepare_entire_test_service import PrepareEntireTest
        self.window = PrepareEntireTest(user)
        self.window.show()

    def gotoEntireTest(self, user, wordIdxList, testChoice):
        print("go to Entire Test Page")
        from entire_test_service import EntireTest
        EntireTest(user, wordIdxList, testChoice)

    def gotoEntireTestResult(self, user, correctIdxList, wrongIdxList):
        print("go to Entire Test Result Page")
        from entire_test_result_service import EntireTestResult
        EntireTestResult(user, correctIdxList, wrongIdxList)

    def gotoMyPage(self, user):
        from my_page_service import MyPage
        self.window = MyPage(user)
        self.window.show()

    def gotoWrongNote(self, user):
        print("go to Wrong Note Page")
        from wrong_note_service import WrongNote
        WrongNote(user)

    def gotoWrongNoteTest(self, user, wordIdxList, testChoice):
        print("go to Wrong Note Test Page")
        from wrong_note_test import WrongNoteTest
        WrongNoteTest(user, wordIdxList, testChoice)

    def gotoWrongNoteTestResult(self, user, correctIdxList, wrongIdxList):
        print("go to Wrong Note Test Result Page")
        from wrong_note_test_result_service import WrongNoteTestResult
        WrongNoteTestResult(user, correctIdxList, wrongIdxList)

    def gotoBookmarkNote(self, user):
        print("go to Bookmark Note Page")
        from bookmark_note_service import BookmarkNote
        BookmarkNote(user)

    def gotoBookmarkNoteTest(self, user, wordIdxList, testChoice):
        print("go to Bookmark Note Test Page")
        from bookmark_note_test_service import BookmarkNoteTest
        BookmarkNoteTest(user, wordIdxList, testChoice)

    def gotoBookmarkNoteTestResult(self, user, correctIdxList, wrongIdxList):
        print("go to Bookmark Note Test Result Page")
        from bookmark_note_test_result_service import BookmarkTestResult
        BookmarkTestResult(user, correctIdxList, wrongIdxList)

    def gotoAfterTestWordNote(self, user, list1, list2, op1, op2):
        print("go to After Test Word Note")
        from after_test_word_note_service import AfterTestWordNote
        AfterTestWordNote(user, list1, list2, op1, op2)

    def gotoManagerPart(self):
        print("go to Manager Part Page")

    def gotoManagerUnit(self):
        print("go to Manager Unit Page")

    def gotoManagerUnitWordNote(self):
        print("go to Manager Unit Word Note Page")

    def gotoManagerAddWord(self):
        print("go to Manager Add Word Page")
