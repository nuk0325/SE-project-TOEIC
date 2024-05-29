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
        # received_word_list = [1,3,5,7,8] # 일단 리스트를 준 상태로 연결
        UnitWordNote(user, partNum, unitNum)

    def gotoPrepareReviewTest(self):
        print("go to Prepare Review Test Page")

    def gotoReviewTest(self, user, wordIdxList, testChoice):
        print("go to Review Test Page")
        from review_test_service import ReviewTest
        ReviewTest(user, wordIdxList, testChoice)

    def gotoReviewTestResult(self):
        print("go to Review Test Result Page")

    def gotoReviewTestCorrectNote(self):
        print("go to Review Test Correct Note Page")

    def gotoReviewTestWrongNote(self):
        print("go to Review Test Wrong Note Page")

    def gotoPrepareEntireTest(self, user):
        print("go to Prepare Entire Test Page")
        from prepare_entire_test_service import PrepareEntireTest
        self.window = PrepareEntireTest(user)
        self.window.show()

    def gotoEntireTest(self):
        print("go to Entire Test Page")

    def gotoEntireTestResult(self):
        print("go to Entire Test Result Page")

    def gotoEntireTestCorrectNote(self):
        print("go to Entire Test Correct Note Page")

    def gotoEntireTestWrongNote(self):
        print("go to Entire Test Wrong Note Page")

    def gotoMyPage(self, user):
        from my_page_service import MyPage
        self.window = MyPage(user)
        self.window.show()

    def gotoWrongNote(self):
        print("go to Wrong Note Page")

    def gotoPrepareWrongNoteTest(self):
        print("go to Prepare Wrong Note Test Page")

    def gotoWrongNoteTest(self):
        print("go to Wrong Note Test Page")

    def gotoWrongNoteTestResult(self):
        print("go to Wrong Note Test Result Page")

    def gotoWrongNoteTestCorrectNote(self):
        print("go to Wrong Note Test Correct Note Page")

    def gotoWrongNoteTestWrongNote(self):
        print("go to Wrong Note Test Wrong Note Page")

    def gotoBookmarkNote(self, user):
        print("go to Bookmark Note Page")
        from bookmark_note_service import BookmarkNote
        BookmarkNote(user)

    def gotoPreapareBookmarkNoteTest(self):
        print("go to Prepare Bookmark Note Test Page")

    def gotoBookmarkNoteTest(self):
        print("go to Bookmark Note Test Page")

    def gotoBookmarkNoteCorrectNote(self):
        print("go to Bookmark Note Correct Note Page")

    def gotoBookmarkNoteWrongNote(self):
        print("go to Bookmark Note Wrong Note Page")

    def gotoManagerPart(self):
        print("go to Manager Part Page")

    def gotoManagerUnit(self):
        print("go to Manager Unit Page")

    def gotoManagerUnitWordNote(self):
        print("go to Manager Unit Word Note Page")

    def gotoManagerAddWord(self):
        print("go to Manager Add Word Page")