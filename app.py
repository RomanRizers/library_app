from flask import Flask, Response, render_template, redirect, url_for, request, send_file
from models.book import Book
from storage.json_storage import JSONStorage
import os


app = Flask(__name__, static_folder="static", template_folder="templates")
storage = JSONStorage()


@app.route("/", methods=["GET"])
def home():
    """Приветсвенная страница"""
    return render_template("home.tpl")


@app.route("/books", methods=["GET"])
def index():
    """Главная страница"""
    search_query = request.args.get("search", "")
    books = storage.get_items()
    if search_query:
        books = [
            book for book in books
            if search_query.lower() in book.title.lower() or
               search_query.lower() in book.author.lower() or
               search_query in str(book.year)
        ]
    return render_template("index.tpl", books=books, search_query=search_query)


@app.route("/add", methods=["GET", "POST"])
def add_book():
    """Добавляет книги."""
    if request.method == "POST":
        book = Book.from_form_data(request.form)
        storage.add(book)
        return redirect(url_for("index"))
    return render_template("add_book.tpl")


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    """Изменяет параметры книги."""
    book = storage.get_item(book_id)
    if request.method == "POST":
        book.update_from_form_data(request.form)
        storage.update(book_id, book)
        return redirect(url_for("index"))
    return render_template("edit_book.tpl", book=book)


@app.route("/delete/<int:book_id>", methods=["POST"])
def delete_book(book_id):
    """Удаляет одну книгу."""
    storage.delete(book_id)
    return redirect(url_for("index"))


@app.route('/delete_all', methods=['POST'])
def delete_all_books():
    """Удаляет все книги."""
    storage.delete_all()
    return redirect(url_for('index'))


@app.route("/download", methods=["GET"])
def download_file():
    """Загрузка JSON файла."""
    filepath = os.path.join("storage", "storage.json")
    if os.path.exists(filepath):
        return send_file(
            filepath,
            as_attachment=True,
            download_name="books.json",
            mimetype="application/json"
        )
    else:
        return Response("Файл не найден", status=404)


if __name__ == "__main__":
    app.run(debug=True)
