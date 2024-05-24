import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt6 import QtCore, QtGui

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 창 크기 설정
        self.setWindowTitle("PyQt6 Basic Window")
        self.setGeometry(100, 100, 360, 600)  # (x, y, width, height)
        
        # 중앙 위젯 설정
        central_widget = QFrame()
        self.setCentralWidget(central_widget)
        
        # 상단 프레임 생성
        top_frame = QFrame(central_widget)
        top_frame.setFixedSize(360, 60)
        
        # 뒤로가기 버튼 생성
        back_button = QPushButton("←", top_frame)
        back_button.setFixedSize(60, 60)
        
        # 홈 버튼 생성
        home_button = QPushButton("🏠", top_frame)
        home_button.setFixedSize(60, 60)
        
        # 중앙 라벨 생성
        note_label = QLabel("복습 테스트", top_frame)
        note_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # 가운데 정렬
        note_label.setFont(QtGui.QFont("Arial", 20))  # 폰트 크기 설정
        
        # 레이아웃 설정
        top_layout = QHBoxLayout(top_frame)
        top_layout.addWidget(back_button)
        top_layout.addWidget(note_label)
        top_layout.addWidget(home_button)
        
        # 하단 프레임 생성
        bottom_frame = QFrame(central_widget)
        bottom_frame.setFixedSize(360, 30)
        
        # 하단 프레임 레이아웃
        bottom_layout = QHBoxLayout(bottom_frame)
        
        # unit_name 라벨 생성
        unit_name_label = QLabel("unit 1", bottom_frame)
        unit_name_label.setFont(QtGui.QFont("Arial", 10))  # 폰트 크기 설정
        bottom_layout.addWidget(unit_name_label)
        
        # Stretch 추가
        bottom_layout.addStretch(1)
        
        # Correct Icon 라벨 생성
        correct_icon_label = QLabel("O", bottom_frame)
        correct_icon_label.setStyleSheet("color: blue;")  # 파란색으로 설정
        correct_icon_label.setFont(QtGui.QFont("Arial", 9))  # 폰트 크기 설정
        bottom_layout.addWidget(correct_icon_label)
        
        # Correct Count 라벨 생성
        correct_count_label = QLabel("10", bottom_frame)
        correct_count_label.setFont(QtGui.QFont("Arial", 9))  # 폰트 크기 설정
        bottom_layout.addWidget(correct_count_label)
        
        # Wrong Icon 라벨 생성
        wrong_icon_label = QLabel("X", bottom_frame)
        wrong_icon_label.setStyleSheet("color: red;")  # 빨간색으로 설정
        wrong_icon_label.setFont(QtGui.QFont("Arial", 9))  # 폰트 크기 설정
        bottom_layout.addWidget(wrong_icon_label)
        
        # Wrong Count 라벨 생성
        wrong_count_label = QLabel("6", bottom_frame)
        wrong_count_label.setFont(QtGui.QFont("Arial", 9))  # 폰트 크기 설정
        bottom_layout.addWidget(wrong_count_label)
        
        # 새로운 프레임 생성
        new_frame = QFrame(central_widget)
        new_frame.setFixedSize(360, 150)

        # 수직 레이아웃 생성
        new_layout = QVBoxLayout(new_frame)

        # wordCount 라벨 생성
        word_count_label = QLabel("5번", new_frame)
        word_count_label.setFont(QtGui.QFont("Arial", 12))  # 폰트 크기 설정
        
        # wordName 라벨 생성
        word_name_label = QLabel("Carbon", new_frame)
        word_name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # 가운데 정렬
        word_name_label.setFont(QtGui.QFont("Arial", 30))  # 폰트 크기 변경
        
        # 라벨들을 수직 레이아웃에 추가
        new_layout.addWidget(word_count_label)
        new_layout.addWidget(word_name_label)
        new_layout.addStretch(1)
        
        # 전체 레이아웃 설정
        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(top_frame)
        main_layout.addWidget(bottom_frame)
        main_layout.addWidget(new_frame)
        main_layout.addStretch(1)  # 중앙, 하단, 새로운 프레임 아래의 공간을 채우기 위해 Stretch 추가

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
