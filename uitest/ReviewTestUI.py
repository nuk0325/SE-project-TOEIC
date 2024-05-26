from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout
from PyQt6 import QtCore, QtGui

class MainWindow(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        # 창 크기 설정
        self.setWindowTitle("PyQt6 Basic Window")
        self.setGeometry(100, 100, 360, 600)  # (x, y, width, height)
        self.centerWindow()
        
        # 중앙 위젯 설정
        central_widget = QFrame()
        self.setCentralWidget(central_widget)
        
        # 상단 프레임 생성
        top_frame = QFrame(central_widget)
        top_frame.setFixedSize(360, 70)
        top_frame.setStyleSheet("background-color: rgba(253, 213, 51, 0.97);")
        
        # 뒤로가기 버튼 생성
        back_button = QPushButton("←", top_frame)
        back_button.setFixedSize(60, 60)
        back_button.clicked.connect(lambda: self.closeAndOpen("back"))
        
        # 홈 버튼 생성
        home_button = QPushButton("🏠", top_frame)
        home_button.setFixedSize(60, 60)
        home_button.clicked.connect(lambda: self.closeAndOpen("home"))
        
        # 중앙 라벨 생성
        self.note_label = QLabel(parent.getTitle(), top_frame)
        self.note_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # 가운데 정렬
        self.note_label.setFont(QtGui.QFont("Arial", 20))  # 폰트 크기 설정
        
        # 레이아웃 설정
        top_layout = QHBoxLayout(top_frame)
        top_layout.addWidget(back_button)
        top_layout.addWidget(self.note_label)
        top_layout.addWidget(home_button)
        
        # 하단 프레임 생성
        bottom_frame = QFrame(central_widget)
        bottom_frame.setFixedSize(360, 30)
        
        # 하단 프레임 레이아웃
        bottom_layout = QHBoxLayout(bottom_frame)
        
        # unit_name 라벨 생성
        self.unit_name_label = QLabel(parent.getUnitNum("unitName"), bottom_frame)
        self.unit_name_label.setFont(QtGui.QFont("Arial", 10))  # 폰트 크기 설정
        bottom_layout.addWidget(self.unit_name_label)
        
        # Stretch 추가
        bottom_layout.addStretch(1)
        
        # Correct Icon 라벨 생성
        correct_icon_label = QLabel("O", bottom_frame)
        correct_icon_label.setStyleSheet("color: blue;")  # 파란색으로 설정
        correct_icon_label.setFont(QtGui.QFont("Arial", 9))  # 폰트 크기 설정
        bottom_layout.addWidget(correct_icon_label)
        
        # Correct Count 라벨 생성
        self.correct_count_label = QLabel(parent.getCorrectCount(), bottom_frame)
        self.correct_count_label.setFont(QtGui.QFont("Arial", 9))  # 폰트 크기 설정
        bottom_layout.addWidget(self.correct_count_label)
        
        # Wrong Icon 라벨 생성
        wrong_icon_label = QLabel("X", bottom_frame)
        wrong_icon_label.setStyleSheet("color: red;")  # 빨간색으로 설정
        wrong_icon_label.setFont(QtGui.QFont("Arial", 9))  # 폰트 크기 설정
        bottom_layout.addWidget(wrong_icon_label)
        
        # Wrong Count 라벨 생성
        self.wrong_count_label = QLabel(parent.getWrongCount(), bottom_frame)
        self.wrong_count_label.setFont(QtGui.QFont("Arial", 9))  # 폰트 크기 설정
        bottom_layout.addWidget(self.wrong_count_label)
        
        # 새로운 프레임 생성
        new_frame = QFrame(central_widget)
        new_frame.setFixedSize(360, 150)

        # 수직 레이아웃 생성
        new_layout = QVBoxLayout(new_frame)

        # wordCount 라벨 생성
        self.word_count_label = QLabel(parent.getWordCountLabel(), new_frame)
        self.word_count_label.setFont(QtGui.QFont("Arial", 12))  # 폰트 크기 설정
        
        # wordName 라벨 생성
        self.word_name_label = QLabel(parent.getWordName(), new_frame)
        self.word_name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # 가운데 정렬
        self.word_name_label.setFont(QtGui.QFont("Arial", 30))  # 폰트 크기 변경
        
        # word_meaning_label 생성
        self.word_meaning_label = QLabel(parent.getMeaning(), new_frame)
        self.word_meaning_label.setFont(QtGui.QFont("Arial", 12))
        self.word_meaning_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_meaning_label.setVisible(False)

        # word_sent_label 생성
        self.word_sent_label = QLabel(parent.getSentence(), new_frame)
        self.word_sent_label.setFont(QtGui.QFont("Arial", 12))
        self.word_sent_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.word_sent_label.setVisible(False)

        # 라벨들을 수직 레이아웃에 추가
        new_layout.addWidget(self.word_count_label)
        #new_layout.addStretch(1)  # Stretch 추가
        new_layout.addWidget(self.word_name_label)
        new_layout.addWidget(self.word_meaning_label)
        new_layout.addWidget(self.word_sent_label)
        new_layout.addStretch(1)  # Stretch 추가

        # 추가 프레임 생성 (360x360)
        self.bottom_large_frame = QFrame(central_widget)
        self.bottom_large_frame.setFixedSize(360, 360)
        
        # 그리드 레이아웃 생성
        self.grid_layout = QGridLayout(self.bottom_large_frame)
        self.grid_layout.setSpacing(10)  # 버튼 사이의 간격 설정
        
        # 버튼 생성 및 그리드 레이아웃에 추가
        self.update_buttons()
        
        # 전체 레이아웃 설정
        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(top_frame)
        main_layout.addWidget(bottom_frame)
        main_layout.addWidget(new_frame)
        main_layout.addWidget(self.bottom_large_frame)
        main_layout.addStretch(1)  # 중앙, 하단, 새로운 프레임 아래의 공간을 채우기 위해 Stretch 추가

    def centerWindow(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

    def closeAndOpen(self, option) :
        self.close()
        if option == "back" :
            self.parent.use_goBack()
        elif option == "home" :
            self.parent.use_gotoHome()
        elif option == "result" :
            self.parent.use_gotoTestResult()
        else :
            print("잘못된 입력입니다.")

    def update_labels_and_buttons(self):
        self.correct_count_label.setText(self.parent.getCorrectCount())
        self.wrong_count_label.setText(self.parent.getWrongCount())
        self.word_count_label.setText(self.parent.getWordCountLabel())
        self.word_name_label.setText(self.parent.getWordName())  # 여기서 word_name_label 업데이트 추가
        self.word_meaning_label.setText(self.parent.getMeaning())
        self.word_sent_label.setText(self.parent.getSentence())
        
        # 기존 버튼 제거
        for i in reversed(range(self.grid_layout.count())): 
            widget_to_remove = self.grid_layout.itemAt(i).widget()
            # remove it from the layout list
            self.grid_layout.removeWidget(widget_to_remove)
            # remove it from the gui
            widget_to_remove.setParent(None)
        
        # 새 버튼 추가
        self.update_buttons()
        


    def update_buttons(self):
        buttonList = self.parent.getMeaningList()
        buttons_info = [(buttonList[0], 1, 1), (buttonList[1], 1, 2), (buttonList[2], 2, 1), (buttonList[3], 2, 2)]
        for text, row, col in buttons_info:
            button = QPushButton(text, self.bottom_large_frame)
            button.setFixedSize(165, 110)
            button.setFont(QtGui.QFont("Arial", 12))  # 폰트 크기 설정
            button.setStyleSheet("background-color: rgb(255, 230, 130);")
            button.clicked.connect(self.on_button_click)   
            self.grid_layout.addWidget(button, row, col)
        
        # "정답보기" 버튼 생성
        answer_button = QPushButton("정답보기", self.bottom_large_frame)
        answer_button.setFixedSize(340, 70)
        answer_button.setFont(QtGui.QFont("Arial", 15))  # 폰트 크기 설정
        answer_button.setStyleSheet("background-color : rgb(224, 224, 224);")
        answer_button.clicked.connect(self.on_button_click)
        self.grid_layout.addWidget(answer_button, 3, 1, 1, 2)  # 3행 1열에 추가하고, span 1x2
        

    def on_button_click(self):
        sender = self.sender()
        if sender:
            self.word_meaning_label.setVisible(True)
            self.word_sent_label.setVisible(True)
            #self.update_buttons()
            QtCore.QTimer.singleShot(3000, self.hide_labels)
            self.parent.afterQuestion(sender.text())
            self.update_labels_and_buttons()  # 버튼을 클릭했을 때 라벨과 버튼을 업데이트합니다.

    def hide_labels(self):
        self.word_meaning_label.setVisible(False)
        self.word_sent_label.setVisible(False)
            
    def changeButtonAndLabel(self) :
        pass