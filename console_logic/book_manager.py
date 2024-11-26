from models.book import Book
from storage.json_storage import JSONStorage

class BookManager:
    def __init__(self):
        self.storage = JSONStorage()


    def show_books(self):
        books = self.storage.get_items()
        if not books:
            print("Нет доступных книг.")
        else:
            print(f"\n{'ID':<5}{'Название':<30}{'Автор':<30}{'Год':<10}{'Статус':<10}")
            for book in books:
                print(f"{book.id:<5}{book.title:<30}{book.author:<30}{book.year:<10}{book.status:<10}")


    def add_book(self):
        """Добавляет книгу в хранилище."""
        title = input("\nВведите название книги: ")
        author = input("Введите автора книги: ")
        year = input("Введите год издания: ")
        
        try:
            year = int(year)
            book = Book(id=id, title=title, author=author, year=year)
            self.storage.add(book)
            print(f"\nКнига '{title}' добавлена!")
        except ValueError:
            print("Ошибка: год должен быть числом.")


    def delete_book(self):
        """Удаляет книгу по ID."""
        self.show_books()
        try:
            book_id = int(input("\nВведите ID книги для удаления: "))
            self.storage.delete(book_id)
            print(f"\nКнига с ID {book_id} удалена!")
        except ValueError:
            print("Ошибка: ID должен быть числом.")


    def update_book(self):
        """Обновляет информацию о книге."""
        self.show_books()
        try:
            book_id = int(input("\nВведите ID книги для обновления: "))
            book = self.storage.get_item(book_id)
            
            if book:
                title = input(f"Новое название книги (оставьте пустым, чтобы не менять): ") or book.title
                author = input(f"Новый автор книги (оставьте пустым, чтобы не менять): ") or book.author
                year = input(f"Новый год издания (оставьте пустым, чтобы не менять): ") or book.year

                try:
                    year = int(year) if year else book.year
                except ValueError:
                    print("Ошибка: год должен быть числом.")
                    return

                status = input(f"Новый статус книги (в наличии/выдана) (оставьте пустым, чтобы не менять): ") or book.status
                if status not in ["в наличии", "выдана"]:
                    print("Ошибка: статус должен быть 'в наличии' или 'выдана'.")
                    return
                
                form_data = {
                    "title": title,
                    "author": author,
                    "year": year,
                    "status": status
                }
                
                book.update_from_form_data(form_data)
                self.storage.update(book_id, book)
                print(f"\nКнига с ID {book_id} обновлена.")
            else:
                print("Книга с таким ID не найдена.")
        except ValueError:
            print("Ошибка: ID должен быть числом.")


    def delete_all_books(self):
        """Удаляет все книги из хранилища."""
        self.storage.delete_all()
        print("\nВсе книги удалены!")


    def save_books_to_txt(self):
        """Сохраняет список книг в текстовый файл."""
        books = self.storage.get_items()
        if not books:
            print("Нет доступных книг для сохранения.")
            return
        
        filename = "books_list.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"{'ID':<5} {'Название':<30} {'Автор':<25} {'Год издания':<15}\n")
            file.write("-" * 80 + "\n")
            for book in books:
                file.write(f"{book.id:<5} {book.title:<30} {book.author:<25} {book.year:<15}\n")
        
        print(f"Список книг сохранен в файл '{filename}'.")
