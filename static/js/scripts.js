function deleteAllBooks() {
    if (confirm("Вы уверены, что хотите удалить все книги?")) {
        fetch("/delete_all", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then(response => {
            if (response.ok) {
                alert("Все книги удалены");
                window.location.href = "/books";
            } else {
                alert("Не удалось удалить книги");
            }
        })
        .catch(error => console.error("Ошибка:", error));
    }
}
