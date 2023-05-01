import datetime


class Note:
    def __init__(self, title, body, note_id=None, date=None):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.date = date or datetime.now()

    def __str__(self):
        return f"{self.title} ({self.date.strftime('%d.%m.%Y %H:%M:%S')})\n{self.body}"
