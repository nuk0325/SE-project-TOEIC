

class toUpdateInManagerService:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def update_word(self, word):
        # DBManager의 update_word_and_remove_wro_fav 메서드를 사용하여 단어를 업데이트하고 wro_fav에서 관련 엔티티를 삭제합니다.
        return self.db_manager.update_word_and_remove_wro_fav(word)

    def delete_word(self, word):
        word.setWordName('0')
        word.setMeaning('0')
        word.setSentence('0')
        self.db_manager.update_word_and_remove_wro_fav(word)

