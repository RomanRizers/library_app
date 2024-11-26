class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status


    def to_dict(self):
        """Преобразует объект книги в словарь."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }


    @classmethod
    def from_dict(cls, data: dict):
        """Создает объект книги из словаря."""
        return cls(
            id=data["id"],
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data.get("status", "в наличии")
        )


    @classmethod
    def from_form_data(cls, form_data):
        """Создание книги из данных формы."""
        try:
            return cls(
                id=int(form_data.get("id", 0)),
                title=form_data["title"],
                author=form_data["author"],
                year=int(form_data["year"]),
                status=form_data.get("status", "в наличии")
            )
        except ValueError:
            raise ValueError("Неверный формат данных года.")


    def update_from_form_data(self, form_data):
        """Обновление данных книги из формы."""
        self.title = form_data.get("title", self.title)
        self.author = form_data.get("author", self.author)
        self.year = int(form_data.get("year", self.year))
        self.status = form_data.get("status", self.status)

