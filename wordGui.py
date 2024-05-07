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

class HomePage(tk.Frame):
    def __init__(self, parent, show_parts_callback):
        super().__init__(parent)
        self.parent = parent

        label = tk.Label(self, text="홈 페이지", font=("Helvetica", 18))
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        button = tk.Button(self, text="학습하기", command=show_parts_callback, width=20, height=5)
        button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

class PartsPage(tk.Frame):
    def __init__(self, parent, show_units_callback, show_home_page_callback):
        super().__init__(parent)
        self.parent = parent

        label = tk.Label(self, text="파트 선택", font=("Helvetica", 18))
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        for idx, part in enumerate(range(1, 9), start=1):
            afterIdx = idx
            if part % 2 == 1:
                button_x = 0.25
            else:
                button_x = 0.75
                afterIdx -= 1
            button = tk.Button(self, text=f"Part {part}", command=lambda part=part: show_units_callback(part), width=20, height=5)
            button.place(relx=button_x, rely=0.2 + afterIdx * 0.1, anchor=tk.CENTER)

        back_button = tk.Button(self, text="뒤로가기", command=show_home_page_callback)
        back_button.place(relx=0.05, rely=0.05, anchor=tk.NW)
        home_button = tk.Button(self, text="홈", command=self.parent.show_home_page)
        home_button.place(relx=0.95, rely=0.05, anchor=tk.NE)

class UnitsPage(tk.Frame):
    def __init__(self, parent, show_words_callback, show_parts_callback):
        super().__init__(parent)
        self.parent = parent
         # 캔버스 및 프레임 추가
        self.canvas = tk.Canvas(self)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # 수직 스크롤바 추가
        scrollbar = tk.Scrollbar(self, command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        label = tk.Label(self, text="유닛 선택", font=("Helvetica", 18))
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        for idx, unit in enumerate(range(1, 16), start=1):
            afterIdx = idx
            if unit % 2 == 1:
                button_x = 0.25
            else:
                button_x = 0.75
                afterIdx -= 1
            button = tk.Button(self, text=f"Unit {unit}", command=lambda unit=unit: show_words_callback(unit), width=20, height=5)
            button.place(relx=button_x, rely=0.2 + afterIdx * 0.06, anchor=tk.CENTER)

        back_button = tk.Button(self, text="뒤로가기", command=show_parts_callback)
        back_button.place(relx=0.05, rely=0.05, anchor=tk.NW)
        home_button = tk.Button(self, text="홈", command=self.parent.show_home_page)
        home_button.place(relx=0.95, rely=0.05, anchor=tk.NE)

class WordsPage(tk.Frame):
    def __init__(self, parent, words, show_units_callback):
        super().__init__(parent)
        self.parent = parent

        self.words = words
        self.meaning_visible = [False] * len(words)

        label = tk.Label(self, text="단어 목록", font=("Helvetica", 18))
        label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        self.word_labels = []
        for idx, (word, _, _, _) in enumerate(self.words, start=1):
            word_label = tk.Label(self, text=word)
            word_label.place(relx=0.5, rely=0.1 + idx * 0.1, anchor=tk.CENTER)
            self.word_labels.append(word_label)

        back_button = tk.Button(self, text="뒤로가기", command=show_units_callback)
        back_button.place(relx=0.05, rely=0.05, anchor=tk.NW)
        home_button = tk.Button(self, text="홈", command=self.parent.show_home_page)
        home_button.place(relx=0.95, rely=0.05, anchor=tk.NE)

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
        self.show_home_page()

    def show_home_page(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = HomePage(self, self.show_parts_page)
        self.current_frame.pack(expand=True, fill=tk.BOTH)

    def show_parts_page(self):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = PartsPage(self, self.show_units_page, self.show_home_page)
        self.current_frame.pack(expand=True, fill=tk.BOTH)

    def show_units_page(self, part):
        if self.current_frame:
            self.current_frame.destroy()

        self.current_frame = UnitsPage(self, lambda unit: self.show_words_page(part, unit), self.show_parts_page)
        self.current_frame.pack(expand=True, fill=tk.BOTH)

    def show_words_page(self, part, unit):
        if self.current_frame:
            self.current_frame.destroy()

        words = self.model.get_words_by_part_and_unit(part, unit)
        words_list = [(row['단어'], row['뜻'], row['예문'], row['예문 뜻']) for idx, row in words.iterrows()]  # 열 이름 수정

        self.current_frame = WordsPage(self, words_list, lambda: self.show_units_page(part))
        self.current_frame.pack(expand=True, fill=tk.BOTH)

if __name__ == "__main__":
    excel_file = r"C:\Users\CHO\toicProject\SE-project-TOEIC\토익멍 영단어리스트.xlsx"
    app = VocabularyApp(excel_file)
    app.mainloop()
