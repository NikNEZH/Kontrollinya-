# -*- coding: utf-8 -*-
import View
import NoteManage
    

# // Вызов приложения
if __name__ == "__main__":
    note_manager = NoteManage.NoteManager("notes.json")
    View.View.__menu__
    # ui = ConsoleUI(note_manager)

    