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

    def gotoEntireTest(self, user, wordIdxList, testChoice):
        print("go to Entire Test Page")
        from entire_test_service import EntireTest
        EntireTest(user, wordIdxList, testChoice)

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

    def gotoWrongNote(self, user):
        print("go to Wrong Note Page")
        from wrong_note_service import WrongNote
        WrongNote(user)

    def gotoPrepareWrongNoteTest(self):
        print("go to Prepare Wrong Note Test Page")

    def gotoWrongNoteTest(self, user, wordIdxList, testChoice):
        print("go to Wrong Note Test Page")
        from wrong_note_test import WrongNoteTest
        WrongNoteTest(user, wordIdxList, testChoice)

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

    def gotoBookmarkNoteTest(self, user, wordIdxList, testChoice):
        print("go to Bookmark Note Test Page")
        from bookmark_note_test_service import BookmarkNoteTest
        BookmarkNoteTest(user, wordIdxList, testChoice)

    def gotoBookmarkNoteTestResult(self, user, correctIdxList, wrongIdxList):
        print("go to Bookmark Note Test Result Page")

    def gotoBookmarkNoteCorrectNote(self):
        print("go to Bookmark Note Correct Note Page")

    def gotoBookmarkNoteWrongNote(self):
        print("go to Bookmark Note Wrong Note Page")

    def gotoManagerPart(self, user):
        print("go to Manager Part Page")
        from manager_part_service import ManagerPart
        self.window = ManagerPart(user)
        self.window.show()

    def gotoManagerUnit(self, partNum, user):
        print("go to Manager Unit Page")
        from manager_unit_service import ManagerUnit
        self.window = ManagerUnit(partNum, user)
        self.window.show()

    def gotoUnitManage(self, partNum, unitNum, user):
        print("go to Manager Unit Word Note Page")
        from UnitManage import UnitManage
        # received_word_list = [1,3,5,7,8] # 일단 리스트를 준 상태로 연결
        UnitManage(user, partNum, unitNum)

    def gotoManagerAddWord(self, line_num):
        print("go to Manager Add Word Page")
        from add_by_manager_service import AddByManagerService
        window = AddByManagerService(line_num)
        window.show()
    
    def gotoManagerUpdateWord(self, line_num, user):
        print("go to Manager Update Word Page")
        from update_by_manager_service import UpdateByManagerService
        window = UpdateByManagerService(line_num)
        window.show()
    '''
    def gotoManagerUpdateWord(self, idx, user):
        # UpdateByManagerService 인스턴스 생성
        from update_by_manager_service import UpdateByManagerService
        from UI.update_by_manager_ui import Ui_UpdateByManagerPage
        update_service = UpdateByManagerService(idx)
        
        # UpdateByManagerService의 setDefaultOfBox 메서드 호출
        update_service.setDefaultOfBox()
        
        # Ui_UpdateByManagerPage 인스턴스 생성
        ui = Ui_UpdateByManagerPage()
        ui.setupUi(update_service)  # UpdateByManagerService 인스턴스를 인자로 전달하여 UI 초기화
    '''
    def gotoMangerSearch(self, user):
        print("gotoMangerSearch")
