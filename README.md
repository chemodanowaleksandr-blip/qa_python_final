# Проект: Тестирование BooksCollector

Реализовано модульное тестирование класса `BooksCollector` с помощью `pytest`.

## Список тестов:
- `test_add_new_book_valid` — Валидное имя книги.
- `test_add_new_book_boundary_values` — Граничные длины (1 и 40 символов).
- `test_add_new_book_empty_name` — Пустое имя.
- `test_add_new_book_too_long_name` — Имя из 41 символа.
- `test_add_duplicate_book` — Проверка на дубликаты книг.
- `test_set_book_genre_valid_genre_success` — Параметризованный тест установки жанров.
- `test_set_book_genre_invalid_genre` — Запрет некорректного жанра.
- `test_set_book_genre_nonexistent_book` — Запрет жанра для несуществующей книги.
- `test_get_book_genre_nonexistent` — Поиск жанра несуществующей книги.
- `test_add_existing_book_to_favorites` — Добавление книги в избранное.
- `test_add_nonexistent_book_to_favorites` — Ошибка добавления несуществующей книги.
- `test_add_duplicate_book_to_favorites` — Исключение дубликатов в избранном.
- `test_delete_book_from_favorites` — Удаление из избранного.
- `test_get_books_with_specific_genre` — Поиск по жанру (sorted).
- `test_get_books_genre_dict` — Получение всего словаря.
- `test_get_books_for_children` — Проверка детских жанров (sorted).
- `test_empty_favorites_list` — Проверка пустого списка избранного.
