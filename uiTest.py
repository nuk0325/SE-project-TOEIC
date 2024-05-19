import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class WordDictionary(QWidget):
    def __init__(self):
        super().__init__()

        # 단어 데이터 (예시)
        word_data = [
            {"word": "apple", "icon": "star.png"},
            {"word": "banana", "icon": "star.png"},
            {"word": "cherry", "icon": "star.png"},
            {"word": "date", "icon": "star.png"},
            {"word": "elderberry", "icon": "star.png"},
            {"word": "fig", "icon": "star.png"},
            {"word": "grape", "icon": "star.png"},
            {"word": "honeydew", "icon": "star.png"},
            {"word": "kiwi", "icon": "star.png"},
            {"word": "lemon", "icon": "star.png"},
            {"word": "mango", "icon": "star.png"},
            {"word": "orange", "icon": "star.png"},
            {"word": "pear", "icon": "star.png"},
            {"word": "quince", "icon": "star.png"},
            {"word": "raspberry", "icon": "star.png"},
            {"word": "strawberry", "icon": "star.png"},
            {"word": "tangerine", "icon": "star.png"},
            {"word": "ugli fruit", "icon": "star.png"},
            {"word": "vanilla bean", "icon": "star.png"},
            {"word": "watermelon", "icon": "star.png"}
        ]

        # 스크롤 가능한 레이아웃
        scroll_layout = QVBoxLayout()

        for data in word_data:
            # 아이콘 및 단어를 가진 QLabel 생성
            label = QLabel()
            label.setPixmap(QPixmap(data["icon"]))
            label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
            label.setText(f" | {data['word']} | ")
            
            # 스크롤 가능한 레이아웃에 추가
            scroll_layout.addWidget(label)

        # 스크롤 가능한 뷰 생성
        scroll_widget = QWidget()
        scroll_widget.setLayout(scroll_layout)

        # 스크롤 영역 설정
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setWidget(scroll_widget)

        # 메인 레이아웃 설정
        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WordDictionary()
    window.show()
    sys.exit(app.exec())
