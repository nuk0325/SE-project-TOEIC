from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        self.answer_button = None

        #타이머 설정
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTimer)
        self.timer.start(1000)  # 1000 밀리초마다 타이머 작동 (1초)
        self.timeCount = 2 #타이머. 문제당 주어진 초
        self.sec = self.timeCount  #문제당 남은 시간. 

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
        self.note_label.setFont(QtGui.QFont("Han Sans", 20))  # 폰트 크기 설정
        
        # 레이아웃 설정
        top_layout = QHBoxLayout(top_frame)
        top_layout.addWidget(back_button)
        top_layout.addWidget(self.note_label)
        top_layout.addWidget(home_button)
        
        # 하단 프레임 생성
        bottom_frame = QFrame(central_widget)
        bottom_frame.setFixedSize(360, 30)
        bottom_frame.setStyleSheet("background-color : white;")
        
        # 하단 프레임 레이아웃
        bottom_layout = QHBoxLayout(bottom_frame)
        
        # 타이머 라벨 생성
        self.unit_name_label = QLabel(f"{self.sec} sec" , bottom_frame)
        self.unit_name_label.setFont(QtGui.QFont("Han Sans", 10))  # 폰트 크기 설정
        self.unit_name_label.setStyleSheet("color: red;") #빨간색으로 변경
        bottom_layout.addWidget(self.unit_name_label)
        
        # Stretch 추가
        bottom_layout.addStretch(1)
        
        # Correct Icon 라벨 생성
        correct_icon_label = QLabel("O", bottom_frame)
        correct_icon_label.setStyleSheet("color: blue;")  # 파란색으로 설정
        correct_icon_label.setFont(QtGui.QFont("Han Sans", 9))  # 폰트 크기 설정
        bottom_layout.addWidget(correct_icon_label)
        
        # Correct Count 라벨 생성
        self.correct_count_label = QLabel(parent.getCorrectCount(), bottom_frame)
        self.correct_count_label.setFont(QtGui.QFont("Han Sans", 9))  # 폰트 크기 설정
        bottom_layout.addWidget(self.correct_count_label)
        
        # Wrong Icon 라벨 생성
        wrong_icon_label = QLabel("X", bottom_frame)
        wrong_icon_label.setStyleSheet("color: red;")  # 빨간색으로 설정
        wrong_icon_label.setFont(QtGui.QFont("Han Sans", 9))  # 폰트 크기 설정
        bottom_layout.addWidget(wrong_icon_label)
        
        # Wrong Count 라벨 생성
        self.wrong_count_label = QLabel(parent.getWrongCount(), bottom_frame)
        self.wrong_count_label.setFont(QtGui.QFont("Han Sans", 9))  # 폰트 크기 설정
        bottom_layout.addWidget(self.wrong_count_label)
        
        # 새로운 프레임 생성
        new_frame = QFrame(central_widget)
        new_frame.setFixedSize(360, 150)
        new_frame.setStyleSheet("background-color : white ;")

        # 수직 레이아웃 생성
        new_layout = QVBoxLayout(new_frame)

        # wordCount 라벨 생성
        self.word_count_label = QLabel(parent.getWordCountLabel(), new_frame)
        self.word_count_label.setFont(QtGui.QFont("Han Sans", 12))  # 폰트 크기 설정
        
        # question 라벨 생성
        self.questionLabel = QLabel(parent.getQuestion(), new_frame)
        self.questionLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # 가운데 정렬
        self.questionLabel.setFont(QtGui.QFont("Han Sans", 30))  # 폰트 크기 변경
        
        # answerLabel 생성
        self.answerLabel = QLabel(parent.getAnswer(), new_frame)
        self.answerLabel.setFont(QtGui.QFont("Han Sans", 12))
        self.answerLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.answerLabel.setVisible(False)

        # sentenceLabel 생성
        self.sentenceLabel = QLabel(parent.getSentence(), new_frame)
        self.sentenceLabel.setFont(QtGui.QFont("Han Sans", 12))
        self.sentenceLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.sentenceLabel.setVisible(False)

        # 라벨들을 수직 레이아웃에 추가
        new_layout.addWidget(self.word_count_label)
        #new_layout.addStretch(1)  # Stretch 추가
        new_layout.addWidget(self.questionLabel)
        new_layout.addWidget(self.answerLabel)
        new_layout.addWidget(self.sentenceLabel)
        new_layout.addStretch(1)  # Stretch 추가

        # 추가 프레임 생성 (360x360)
        self.bottom_large_frame = QFrame(central_widget)
        self.bottom_large_frame.setFixedSize(360, 360)
        self.bottom_large_frame.setStyleSheet("background-color : white;")
        
        # 그리드 레이아웃 생성
        self.grid_layout = QGridLayout(self.bottom_large_frame)
        self.grid_layout.setSpacing(10)  # 버튼 사이의 간격 설정
        
        # 버튼 생성 및 그리드 레이아웃에 추가
        self.update_labels_and_buttons() #버튼이 클릭된다면. 
        
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
            self.parent.use_gotoSelectTestResult()
        else :
            print("잘못된 입력입니다.")

    def updateTimer(self):
        # sec 값 감소 및 QLabel 업데이트
        if self.sec > 0:
            self.sec -= 1
            self.unit_name_label.setText(f"{self.sec} sec")
        else:
            #타이머 멈추기
            self.timer.stop()

            #정답보기 버튼을 클릭했다 처리
            self.answer_button.click() 

    def initTimer(self):
        #타이머 초기화. 재시작
        self.timer.start(1000)
        self.sec = self.timeCount
        self.unit_name_label.setText(f"{self.sec} sec")

    def update_labels_and_buttons(self):
        self.correct_count_label.setText(self.parent.getCorrectCount())
        self.wrong_count_label.setText(self.parent.getWrongCount())
        self.word_count_label.setText(self.parent.getWordCountLabel())
        self.questionLabel.setText(self.parent.getQuestion())  # 여기서 questionLabel 업데이트 추가
        self.answerLabel.setText(self.parent.getAnswer())
        self.sentenceLabel.setText(self.parent.getSentence())
        
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
            button.setFont(QtGui.QFont("Han Sans", 12))  # 폰트 크기 설정
            button.setStyleSheet("background-color: rgb(255, 230, 130);")
            button.clicked.connect(self.on_button_click)   
            self.grid_layout.addWidget(button, row, col)
        
        # "정답보기" 버튼 생성
        self.answer_button = QPushButton("정답보기", self.bottom_large_frame)
        self.answer_button.setFixedSize(340, 70)
        self.answer_button.setFont(QtGui.QFont("Han Sans", 15))  # 폰트 크기 설정
        self.answer_button.setStyleSheet("background-color : rgb(224, 224, 224);")
        self.answer_button.clicked.connect(self.on_button_click)
        
        self.grid_layout.addWidget(self.answer_button, 3, 1, 1, 2)  # 3행 1열에 추가하고, span 1x2
        

    def on_button_click(self):
        self.timer.stop() #타이머 멈추기
        sender = self.sender()
        if sender:
            self.lookAnswer(sender)
            QtCore.QTimer.singleShot(500, self.hide_labels) # 3초 뒤에 전체 이벤트가 실행되도록 고쳐보자
            QtCore.QTimer.singleShot(500, lambda: self.checkBoolean(sender))

    def hide_labels(self):
        self.answerLabel.setVisible(False)
        self.sentenceLabel.setVisible(False)
            
    def checkBoolean(self, sender) :
        text = sender.text()
        boolean = self.parent.afterQuestion(text)
        if boolean :
            self.update_labels_and_buttons()  # 버튼을 클릭했을 때 라벨과 버튼을 업데이트합니다.
            self.initTimer()
        else :
            self.timer.stop()
            self.closeAndOpen("result")
    
    def lookAnswer(self, sender) :
        self.answerLabel.setVisible(True)
        self.sentenceLabel.setVisible(True)
        correct_meaning = self.parent.getAnswer()
        for button in self.bottom_large_frame.findChildren(QPushButton):
            if button.text() == correct_meaning:
                button.setStyleSheet("background-color: green;")
                if button != sender :
                    sender.setStyleSheet("background-color: red;")