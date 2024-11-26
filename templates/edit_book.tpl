{% extends "base.tpl" %}

{% block content %}
<h2 style="text-align: center; margin-bottom: 20px;">Редактировать книгу</h2>
<div class="container">
    <form action="{{ url_for('edit_book', book_id=book.id) }}" method="post">
        <label for="title">Название книги:</label>
        <input type="text" id="title" name="title" value="{{ book.title }}" required>

        <label for="author">Автор:</label>
        <input type="text" id="author" name="author" value="{{ book.author }}" required>

        <label for="year">Год издания:</label>
        <input type="number" id="year" name="year" value="{{ book.year }}" required>

        <label for="status">Статус:</label>
        <select id="status" name="status">
            <option value="в наличии" {% if book.status == "в наличии" %}selected{% endif %}>В наличии</option>
            <option value="выдана" {% if book.status == "выдана" %}selected{% endif %}>Выдана</option>
        </select>

        <button type="submit">Сохранить изменения</button>
    </form>
</div>
{% endblock %}
