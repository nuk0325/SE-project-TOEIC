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

    def gotoMyPage(self):
        print("go to My Page")
        from my_page_service import MyPage
        self.window = MyPage()
        self.window.show()

    def gotoUserPart(self):
        print("go to User Part Page")
        from user_part_service import UserPart
        self.window = UserPart()
        self.window.show()

    def gotoUserUnit(self, partNum):
        print("go to User Unit Page")
        from user_unit_service import UserUnit
        self.window = UserUnit(partNum)
        self.window.show()

    def gotoUnitWordNote(self, partNum, unitNum):
        print("go to Unit Word Note Page")
        from unit_word_note_service import UnitWordNote
        received_word_list = [1,3,5,7,8]
        self.window = UnitWordNote(received_word_list)
        self.window.show()

    def gotoPrepareReviewTest(self):
        print("go to Prepare Review Test Page")

    def gotoReviewTest(self):
        from service.review_test_service import ReviewTest
        self.window = ReviewTest()
        self.window.show()

    def gotoReviewTestResult(self):
        print("go to Review Test Result Page")

    def gotoReviewTestCorrectNote(self):
        print("go to Review Test Correct Note Page")

    def gotoReviewTestWrongNote(self):
        print("go to Review Test Wrong Note Page")

    def gotoPrepareEntireTest(self):
        print("go to Prepare Entire Test Page")
        from prepare_entire_test_service import 

    def gotoEntireTest(self):
        print("go to Entire Test Page")

    def gotoEntireTestResult(self):
        print("go to Entire Test Result Page")

    def gotoEntireTestCorrectNote(self):
        print("go to Entire Test Correct Note Page")

    def gotoEntireTestWrongNote(self):
        print("go to Entire Test Wrong Note Page")

    def gotoMyPage(self):
        from my_page_service import MyPage
        self.window = MyPage()
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

    def gotoBookmarkNote(self):
        print("go to Bookmark Note Page")

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
