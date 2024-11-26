import json
import os
from typing import List, Optional
from models.book import Book
from storage.storage_strategy import StorageStrategy


class JSONStorage(StorageStrategy):
    def __init__(self):
        self.storage_dir = "storage"
        os.makedirs(self.storage_dir, exist_ok=True)
        self.filename = os.path.join(self.storage_dir, "storage.json")
        self.items = []
        self.load()


    def load(self):
        """Загружает данные из JSON файла, если он существует."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    self.items = [Book(**item) for item in data]
                    print(f"Загруженные данные: {data}")
            except json.JSONDecodeError as e:
                print(f"Ошибка загрузки JSON файла: {e}")
                self.items = []
            except IOError as e:
                print(f"Ошибка при чтении файла: {e}")
                self.items = []
            except Exception as e:
                print(f"Неизвестная ошибка: {e}")
                self.items = []
        else:
            print("Файл не найден. Загрузка будет без него.")


    def save(self):
        """Сохраняет данные в JSON файл."""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                data = [book.to_dict() for book in self.items]
                json.dump(data, file, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Ошибка при записи в файл: {e}")
        except Exception as e:
            print(f"Неизвестная ошибка при сохранении: {e}")


    def get_items(self) -> List[Book]:
        """Возвращает все книги."""
        return self.items


    def add(self, item: Book):
        """Добавляет книгу в список и сохраняет изменения."""
        try:
            id_book = max([book.id for book in self.items], default=0) + 1
            item.id = id_book
            self.items.append(item)
            self.save()
        except Exception as e:
            print(f"Ошибка при добавлении книги: {e}")


    def delete(self, item_id: int):
        """Удаляет книгу по ID и сохраняет изменения."""
        try:
            self.items = [item for item in self.items if item.id != item_id]
            self.save()
        except Exception as e:
            print(f"Ошибка при удалении книги: {e}")


    def delete_all(self):
        """Удаляет все книги и сохраняет изменения."""
        try:
            self.items.clear()
            self.save()
        except Exception as e:
            print(f"Ошибка при удалении всех книг: {e}")


    def update(self, item_id: int, updated_item: Book):
        """Обновляет данные книги по ID и сохраняет изменения."""
        try:
            for i, item in enumerate(self.items):
                if item.id == item_id:
                    self.items[i] = updated_item
                    break
            self.save()
        except Exception as e:
            print(f"Ошибка при обновлении книги: {e}")


    def get_item(self, item_id: int) -> Optional[Book]:
        """Возвращает книгу по ID, или None, если не найдена."""
        try:
            for item in self.items:
                if item.id == item_id:
                    return item
        except Exception as e:
            print(f"Ошибка при поиске книги: {e}")
        return None
