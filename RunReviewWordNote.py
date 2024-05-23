from ReviewWordNote import ReviewWordNote
from uitest.WordNoteUI import MainWindow

if __name__ == "__main__": # UI 실행 코드
    received_word_list = [1,3,5,7,8]  # 받은 단어 목록을 입력하세요.
    reviewWordNote = ReviewWordNote(received_word_list)
    reviewWordNote.main()