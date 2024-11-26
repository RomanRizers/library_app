<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Сервис управления книгами</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <header>
        <h1>Сервис управления книгами</h1>
        <nav>
            <a href="{{ url_for('home') }}">Главная</a> |
            <a href="{{ url_for('add_book') }}">Добавить книгу</a> |
            <a href="{{ url_for('download_file') }}">Скачать JSON</a> |
            <a href="{{ url_for('delete_all_books') }}">Удалить все книги</a>
        </nav>
    </header>

    <div class="container">
        <!-- Форма поиска -->
        <div class="search-form">
            <form method="get" action="{{ url_for('index') }}">
                <input type="text" name="search" placeholder="Поиск по названию, автору или году" value="{{ search_query }}">
                <button type="submit">Найти</button>
            </form>
        </div>

        <!-- Таблица с книгами -->
        <div class="table-responsive">
            <table>
                <thead>
                    <tr>
                        <th>Название</th>
                        <th>Автор</th>
                        <th>Год</th>
                        <th>Статус</th>
                        <th>Действия</th>
                    </tr>
                </thead>
                <tbody>
                    {% for book in books %}
                        <tr>
                            <td>{{ book.title }}</td>
                            <td>{{ book.author }}</td>
                            <td>{{ book.year }}</td>
                            <td>{{ book.status }}</td>
                            <td class="actions">
                                <!-- Ссылка на редактирование -->
                                <a href="{{ url_for('edit_book', book_id=book.id) }}">Редактировать</a>
                                <form id="delete-form-{{ book.id }}" action="{{ url_for('delete_book', book_id=book.id) }}" method="POST" style="display: inline;">
                                    <a href="#" onclick="document.getElementById('delete-form-{{ book.id }}').submit();" style="color: red;">Удалить</a>
                                </form>
                            </td>
                            
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
