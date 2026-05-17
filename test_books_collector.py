import pytest
from books_collector import BooksCollector


class TestBooksCollector:

    def test_add_new_book_valid(self):
        """Успешное добавление книги с валидным названием"""
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        assert "Война и мир" in collector.get_books_genre()
        assert collector.get_book_genre("Война и мир") == ''

    @pytest.mark.parametrize("book_name", [
        "A",                  # Граничное значение: 1 символ
        "a" * 40,             # Граничное значение: 40 символов
    ])
    def test_add_new_book_boundary_values(self, book_name):
        """Добавление книги с граничной длиной названия (1 и 40 символов)"""
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    def test_add_new_book_empty_name(self):
        """Попытка добавления книги с пустым названием (0 символов)"""
        collector = BooksCollector()
        collector.add_new_book("")
        assert "" not in collector.get_books_genre()

    def test_add_new_book_too_long_name(self):
        """Попытка добавления книги с названием длиннее 40 символов (41 символ)"""
        collector = BooksCollector()
        collector.add_new_book("a" * 41)
        assert "a" * 41 not in collector.get_books_genre()

    def test_add_duplicate_book(self):
        """Повторное добавление одной и той же книги невозможно"""
        collector = BooksCollector()
        collector.add_new_book("Дюна")
        collector.set_book_genre("Дюна", "Фантастика")
        collector.add_new_book("Дюна")
        assert collector.get_book_genre("Дюна") == "Фантастика"

    @pytest.mark.parametrize("book_name, genre", [
        ("1984", "Фантастика"),
        ("Мастер и Маргарита", "Ужасы"),
        ("Шерлок Холмс", "Детективы")
    ])
    def test_set_book_genre_valid_genre_success(self, book_name, genre):
        """Успешная установка валидного жанра из списка разрешенных"""
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_set_book_genre_invalid_genre(self):
        """Попытка установить несуществующий в списке genre жанр"""
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Классика")
        assert collector.get_book_genre("Война и мир") == ''

    def test_set_book_genre_nonexistent_book(self):
        """Попытка установить жанр для книги, которой нет в коллекции"""
        collector = BooksCollector()
        collector.set_book_genre("Неизвестная книга", "Фантастика")
        assert "Неизвестная книга" not in collector.get_books_genre()

    def test_get_book_genre_nonexistent(self):
        """Получение жанра несуществующей книги возвращает None"""
        collector = BooksCollector()
        assert collector.get_book_genre("Неизвестная книга") is None

    def test_add_existing_book_to_favorites(self):
        """Позитивный сценарий: добавление существующей в коллекции книги в избранное"""
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        assert "Гарри Поттер" in collector.get_list_of_favorites_books()

    def test_add_nonexistent_book_to_favorites(self):
        """Негативный сценарий: книгу нельзя добавить в избранное, если её нет в коллекции"""
        collector = BooksCollector()
        collector.add_book_in_favorites("Неизвестная книга")
        assert "Неизвестная книга" not in collector.get_list_of_favorites_books()

    def test_add_duplicate_book_to_favorites(self):
        """Повторное добавление книги в избранное не создает дубликат в списке"""
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        assert collector.get_list_of_favorites_books() == ["Гарри Поттер"]

    def test_delete_book_from_favorites(self):
        """Успешное удаление книги из избранного"""
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.delete_book_from_favorites("Гарри Поттер")
        assert "Гарри Поттер" not in collector.get_list_of_favorites_books()

    def test_get_books_with_specific_genre(self):
        """Получение списка книг определенного жанра"""
        collector = BooksCollector()
        collector.add_new_book("Дюна")
        collector.add_new_book("451 градус")
        collector.set_book_genre("Дюна", "Фантастика")
        collector.set_book_genre("451 градус", "Фантастика")
        
        result = collector.get_books_with_specific_genre("Фантастика")
        assert sorted(result) == sorted(["Дюна", "451 градус"])

    def test_get_books_genre_dict(self):
        """Получение всего словаря книг и их жанров"""
        collector = BooksCollector()
        collector.add_new_book("Дюна")
        collector.set_book_genre("Дюна", "Фантастика")
        assert collector.get_books_genre() == {"Дюна": "Фантастика"}

    def test_get_books_for_children(self):
        """Возвращаются только книги без возрастного ограничения"""
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.add_new_book("Король Лев")
        collector.add_new_book("Смешарики")
        collector.set_book_genre("Оно", "Ужасы")
        collector.set_book_genre("Король Лев", "Мультфильмы")
        collector.set_book_genre("Смешарики", "Комедии")
        
        result = collector.get_books_for_children()
        assert sorted(result) == sorted(["Король Лев", "Смешарики"])

    def test_empty_favorites_list(self):
        """По умолчанию список избранного пуст"""
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []
