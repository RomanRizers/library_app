from storage.json_storage import JSONStorage
from console_logic.book_manager import BookManager

storage = JSONStorage()

class ConsoleApp:
    def __init__(self):
        self.manager = BookManager()

    def print_menu(self):
        """Отображает меню с разделителями."""
        menu = [
            ["Показать все книги", self.manager.show_books],
            ["Добавить книгу", self.manager.add_book],
            ["Удалить книгу", self.manager.delete_book],
            ["Обновить книгу", self.manager.update_book],
            ["Удалить все книги", self.manager.delete_all_books],
            ["Сохранить книги в файл", self.manager.save_books_to_txt],
            ["Выход", self.exit]
        ]
        
        print("\n" + "-" * 40)
        print("Меню:")
        for i, (action, _) in enumerate(menu, start=1):
            print(f"{i}. {action}")
        print("-" * 40)
        
        return menu

    def exit(self):
        """Завершается выполнение программы."""
        print("\nВыход из приложения.")
        exit()

    def run(self):
        """Запускает основное меню приложения."""
        while True:
            self.print_menu()
            choice = input("Выберите действие (1-7): ")
            
            if choice.isdigit() and 1 <= int(choice) <= 7:
                menu = self.print_menu()
                action = menu[int(choice) - 1][1]
                action()
            else:
                print("Некорректный выбор. Пожалуйста, выберите от 1 до 7.")

if __name__ == "__main__":
    app = ConsoleApp()
    app.run()

