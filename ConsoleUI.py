class ConsoleUI:
    def __init__(self, note_manager):
        self.note_manager = note_manager

    def show_notes(self):
        for note in self.note_manager.notes:
            print(note)
            print()

    def add_note(self):
        title = input("Введите название заметки: ")
        body = input("Введите текст заметки: ")
        self.note_manager.add_note(title, body)
        print("Примечание добавлено")

    def edit_note(self):
        note_id = int(input("Введите идентификатор заметки (id ): "))
        title = input("Введите новый заголовок (оставьте пустым, чтобы оставить старый): ")
        body = input("Введите новое тело (оставьте пустым, чтобы оставить старое): ")
        self.note_manager.edit_note(note_id, title, body)
        print("Примечание изменено")

    def delete_note(self):
        note_id = int(input("Enter note id: "))
        self.note_manager.delete_note(note_id)
        print("Примечание изменено")

    def search_notes(self):
        search_query = input("Введите поисковый запрос: ")
        results = self.note_manager.search_notes(search_query)
        print(f"Найденное {len(results)} примечание:")
        for note in results:
            print(note)
            print()