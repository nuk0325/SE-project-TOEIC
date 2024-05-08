import tkinter as tk
from tkinter import ttk
import pandas as pd

class VocabularyModel:
    def __init__(self, excel_file):
        self.vocabulary_df = pd.read_excel(excel_file)

    def get_words_by_part_and_unit(self, part, unit):
        part_start_index = (part - 1) * 150
        part_end_index = part_start_index + 150
        part_df = self.vocabulary_df.iloc[part_start_index:part_end_index]
        unit_start_index = (unit - 1) * 10
        unit_end_index = unit_start_index + 10
        unit_words = part_df.iloc[unit_start_index:unit_end_index]
        return unit_words[['단어', '뜻','예문','예문 뜻']]
#뒤로가기, 홈 베이스 추가
class BasePage(tk.Frame):
    def __init__(self, parent, title):
        super().__init__(parent)
        self.parent = parent
        self.title = title

        label = tk.Label(self, text=title, font=("Helvetica", 18))
        label.pack(pady=20)  # Add padding at the top

        back_button = tk.Button(self, text="뒤로가기", command=self.go_back)
        back_button.pack(side=tk.LEFT, padx=10, pady=5, anchor=tk.NW)  # Anchor to the northwest corner
        
        home_button = tk.Button(self, text="홈", command=self.go_home)
        home_button.pack(side=tk.RIGHT, padx=10, pady=5, anchor=tk.NE)  # Anchor to the northeast corner

        # 추가: 라벨의 높이를 기준으로 버튼을 정렬
        self.update_idletasks()  # 위젯들의 크기와 위치가 업데이트되도록 호출
        title_height = label.winfo_height()  # 타이틀 라벨의 높이 가져오기
        back_button.place(relx=0, rely=0, anchor=tk.NW, y=title_height)  # 뒤로가기 버튼을 최 상단에 배치
        home_button.place(relx=1, rely=0, anchor=tk.NE, y=title_height)  # 홈 버튼을 최 상단에 배치

    def go_back(self):
        self.parent.show_previous_page()

    def go_home(self):
        self.parent.show_home_page()


class HomePage(BasePage):
    def __init__(self, parent):
        super().__init__(parent, "홈 페이지")

        button = tk.Button(self, text="학습하기", command=self.go_to_parts_page, width=20, height=5)
        button.pack()

    def go_to_parts_page(self):
        self.parent.show_parts_page()

class PartsPage(BasePage):
    def __init__(self, parent):
        super().__init__(parent, "파트 선택")

        for idx, part in enumerate(range(1, 9), start=1):
            afterIdx = idx
            if part % 2 == 1:
                button_x = 0.25
            else:
                button_x = 0.75
                afterIdx -= 1
            button = tk.Button(self, text=f"Part {part}", command=lambda part=part: self.go_to_units_page(part), width=20, height=5)
            button.place(relx=button_x, rely=0.2 + afterIdx * 0.1, anchor=tk.CENTER)

    def go_to_units_page(self, part):
        self.parent.show_units_page(part)

class UnitsPage(BasePage):
    def __init__(self, parent, part):
        super().__init__(parent, "유닛 선택")
        self.part = part  # 인스턴스 변수로 'part' 저장

        for idx, unit in enumerate(range(1, 16), start=1):
            afterIdx = idx
            if unit % 2 == 1:
                button_x = 0.25
            else:
                button_x = 0.75
                afterIdx -= 1
            button = tk.Button(self, text=f"Unit {unit}", command=lambda unit=unit: self.go_to_words_page(unit), width=20, height=5)
            button.place(relx=button_x, rely=0.2 + afterIdx * 0.06, anchor=tk.CENTER)

    def go_to_words_page(self, unit):
        self.parent.show_words_page(unit)  # 'part'를 함께 전달하지 않음

class WordsPage(BasePage):
    def __init__(self, parent, words):
        super().__init__(parent, "단어 목록")

        self.words = words
        self.meaning_visible = [False] * len(words)

        self.word_labels = []
        for idx, (word, _, _, _) in enumerate(self.words, start=1):
            word_label = tk.Label(self, text=word)
            word_label.place(relx=0.5, rely=0.1 + idx * 0.1, anchor=tk.CENTER)
            self.word_labels.append(word_label)

        self.show_meaning_buttons = []
        for idx, _ in enumerate(self.words):
            show_meaning_button = tk.Button(self, text="뜻", command=lambda idx=idx: self.toggle_meaning(idx))
            show_meaning_button.place(relx=0.9, rely=0.2 + idx * 0.1, anchor=tk.CENTER)
            self.show_meaning_buttons.append(show_meaning_button)

    def toggle_meaning(self, idx):
        self.meaning_visible[idx] = not self.meaning_visible[idx]
        if self.meaning_visible[idx]:
            self.word_labels[idx].config(text=f"{self.words[idx][0]}\n {self.words[idx][1]}\n {self.words[idx][2]}\n {self.words[idx][3]}")
            self.show_meaning_buttons[idx].config(text="뜻 닫기")  # "뜻 닫기"로 변경
        else:
            self.word_labels[idx].config(text=self.words[idx][0])
            self.show_meaning_buttons[idx].config(text="뜻")  # "뜻"으로 변경

class VocabularyApp(tk.Tk):
    def __init__(self, excel_file):
        super().__init__()
        self.title("TOEIC Vocabulary")
        self.geometry("500x800")

        self.model = VocabularyModel(excel_file)

        self.current_frame = None
        self.page_stack = []  # 페이지 이동 기록을 관리하는 스택

        self.show_home_page()

    def show_previous_page(self):
        if len(self.page_stack) > 1:  # 최소 두 개의 페이지가 스택에 있어야 뒤로 갈 수 있음
            self.page_stack.pop()  # 현재 페이지를 스택에서 제거
            if self.current_frame:
                self.current_frame.destroy()  # 현재 프레임을 제거
            prev_page_class, prev_part = self.page_stack[-1]  # 이전 페이지의 클래스와 'part' 가져오기
            prev_page = prev_page_class(self, prev_part)  # 이전 페이지의 인스턴스 생성, 'part' 전달
            self.current_frame = prev_page  # 현재 프레임을 이전 페이지로 설정
            self.current_frame.pack(expand=True, fill=tk.BOTH)  # 이전 페이지를 보여줌


    def show_page(self, page):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = page
        self.current_frame.pack(expand=True, fill=tk.BOTH)

    def show_home_page(self):
        home_page = HomePage(self)
        self.page_stack = [(HomePage, None)]  # 홈 페이지 클래스와 'part' 없음을 스택에 추가
        self.show_page(home_page)


    def show_parts_page(self):
        if self.current_frame:
            self.current_frame.destroy()

        parts_page = PartsPage(self)
        self.page_stack.append((PartsPage, None))  # 스택에 현재 페이지 클래스와 'part' 없음 추가
        self.show_page(parts_page)

    def show_units_page(self, part):
        if self.current_frame:
            self.current_frame.destroy()

        units_page = UnitsPage(self, part)
        self.page_stack.append((UnitsPage, part))  # 스택에 현재 페이지 클래스와 선택한 'part' 추가
        self.show_page(units_page)

    def show_words_page(self, unit):
        if self.current_frame:
            self.current_frame.destroy()

        words = self.model.get_words_by_part_and_unit(self.page_stack[-1][1], unit)
        words_list = [(row['단어'], row['뜻'], row['예문'], row['예문 뜻']) for idx, row in words.iterrows()]  # 열 이름 수정

        words_page = WordsPage(self, words_list)
        self.page_stack.append((WordsPage, self.page_stack[-1][1]))  # 스택에 현재 페이지 클래스와 선택한 'part' 추가
        self.show_page(words_page)

if __name__ == "__main__":
    excel_file = r"C:\Users\CHO\toicProject\hun\toicPojectSH\토익멍 영단어리스트.xlsx"
    app = VocabularyApp(excel_file)
    app.mainloop()
