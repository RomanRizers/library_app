from abc import ABC, abstractmethod
from typing import List
from models.book import Book

class StorageStrategy(ABC):
    @abstractmethod
    def get_items(self) -> List[Book]:
        pass

    @abstractmethod
    def add(self, item: Book):
        pass

    @abstractmethod
    def delete(self, item_id: int):
        pass

    @abstractmethod
    def update(self, item_id: int, item: Book):
        pass

    @abstractmethod
    def get_item(self, item_id: int) -> Book:
        pass

    @abstractmethod
    def delete_all(self):
        pass
    
    @abstractmethod
    def load(self):
        pass
    
    @abstractmethod
    def save(self):
        pass