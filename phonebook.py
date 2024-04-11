# 전화번호부 프로그램
# 연락처를 추가, 검색, 삭제 할 수 있음
# 연락처를 추가, 삭제 했을 때 txt 파일에 변경사항 저장.

class Phonebook:
    def __init__(self, filename="phonebook.txt"):
        self.filename = filename
        self.contacts = {}

    def load_phonebook(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    name, number = line.strip().split(":")
                    self.contacts[name] = number
        except FileNotFoundError:
            pass

    def save_phonebook(self):
        with open(self.filename, "w") as file:
            for name, number in self.contacts.items():
                file.write(f"{name}:{number}\n")

    def add_contact(self):
        name = input("이름을 입력하세요: ")
        number = input("전화번호를 입력하세요: ")
        if name in self.contacts:
            print("이미 존재하는 연락처입니다.")
        else:
            self.contacts[name] = number
            print(f"{name} 님의 전화번호 {number} 가 추가되었습니다.")

    def delete_contact(self):
        name = input("삭제할 이름을 입력하세요: ")
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name} 님의 연락처가 삭제되었습니다.")
        else:
            print(f"{name} 님의 연락처를 찾을 수 없습니다.")

    def search_contact(self):
        name = input("검색할 이름을 입력하세요: ")
        if name in self.contacts:
            print(f"{name} 님의 전화번호는 {self.contacts[name]} 입니다.")
        else:
            print(f"{name} 님의 연락처를 찾을 수 없습니다.")

    def run(self):
        self.load_phonebook()

        while True:
            print("\n옵션:")
            print("1. 연락처 추가")
            print("2. 연락처 삭제")
            print("3. 연락처 검색")
            print("4. 종료")

            choice = input("원하는 작업을 선택하세요: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.delete_contact()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                print("프로그램을 종료합니다...")
                self.save_phonebook()
                break
            else:
                print("잘못된 선택입니다. 다시 선택해주세요.")


phonebook_manager = Phonebook()
phonebook_manager.run()
