import json
import Note
import NoteEncoder

class NoteManager:
    def __init__(self, filename):
        self.filename = filename
        self.notes = []
        self._load_notes()
        self.encoder = NoteEncoder()
        self.note_id_counter = len(self.notes)

    def _load_notes(self):
        try:
            with open(self.filename, "r", encoding='utf-8') as f:
                notes_data = json.load(f)
            for note_data in notes_data:
                self.notes.append(Note(**note_data))
        except FileNotFoundError:
            pass

    def _save_notes(self):
        notes_data = [{"title": note.title, "body": note.body, "note_id": note.note_id, "date": self.encoder.encode(note.date)} for note in self.notes]
        with open(self.filename, "w", encoding='utf-8') as f:
            json.dump(notes_data, f, indent=5, ensure_ascii=False)

    def add_note(self, title, body):
        self.note_id_counter += 1
        self.notes.append(Note(title, body, self.note_id_counter))
        self._save_notes()

    def edit_note(self, note_id, title=None, body=None):
        note = self.get_note_by_id(note_id)
        if title:
            note.title = title
        if body:
            note.body = body
        self._save_notes()

    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)
        self.notes.remove(note)
        self._save_notes()

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        raise ValueError("Такой записи НЕТУ ЧУВАК!!!")

    def search_notes(self, search_query):
        results = []
        for note in self.notes:
            if search_query in note.title or search_query in note.body:
                results.append(note)
        return results