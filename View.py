from ConsoleUI import ConsoleUI
from NoteManage import NoteManager
ui = ConsoleUI(NoteManager)

# Вызываем меню через отдельный класс
class View: 
    def __menu__():
        while True:
            print("Menu:")
            print("1. Show notes")
            print("2. Add note")
            print("3. Edit note")
            print("4. Delete note")
            print("5. Search notes")
            print("6. Exit")
            
            choice = input("Enter choice: ")
            if choice == "1":
                ui.show_notes()
            elif choice == "2":
                ui.add_note()
            elif choice == "3":
                ui.edit_note()
            elif choice == "4":
                ui.delete_note()
            elif choice == "5":
                ui.search_notes()
            elif choice == "6":
                break
            else:
                print("Invalid choice")