{% extends "base.tpl" %}

{% block content %}
<h2 style="text-align: center; margin-bottom: 20px;">Добавить новую книгу</h2>
<div class="container">
    <form action="{{ url_for('add_book') }}" method="post">
        <label for="title">Название книги:</label>
        <input type="text" id="title" name="title" required>

        <label for="author">Автор:</label>
        <input type="text" id="author" name="author" required>

        <label for="year">Год издания:</label>
        <input type="number" id="year" name="year" required>

        <!-- Статус книги фиксированный -->
        <input type="hidden" name="status" value="в наличии">

        <button type="submit">Добавить</button>
    </form>
</div>
{% endblock %}
