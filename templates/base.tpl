<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <script src="{{ url_for('static', filename='js/scripts.js') }}"></script>
    <header>
        <h1>Сервис управления книгами</h1>
        <nav>
            <a href="{{ url_for('home') }}">Главная</a> |
            <a href="{{ url_for('index') }}">Таблица книг</a> |
            <a href="{{ url_for('add_book') }}">Добавить книгу</a> |
            <a href="{{ url_for('download_file') }}">Скачать JSON</a> |
            <a href="#" onclick="deleteAllBooks()">Удалить все книги</a>
        </nav>        
    </header>
    <div class="container">
        {% block content %}
        {% endblock %}
    </div>
</body>
</html>
