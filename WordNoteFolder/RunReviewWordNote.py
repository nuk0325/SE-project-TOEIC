from ReviewWordNote import ReviewWordNote
from uitest.WordNoteUI import MainWindow

if __name__ == "__main__": # UI 실행 코드
    received_word_list = []
    for i in range(50) :
        received_word_list.append(i+1)
    reviewWordNote = ReviewWordNote(received_word_list)