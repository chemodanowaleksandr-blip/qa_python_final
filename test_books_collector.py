import pytest
from books_collector import BooksCollector

class TestBooksCollector:

    def test_add_new_book_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        assert 'Война и мир' in collector.get_books_genre()
        assert collector.get_book_genre('Война и мир') == ''

    @pytest.mark.parametrize('book_name', [
        "A",
        "a" * 40,
    ])
    def test_add_new_book_boundary_values(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    def test_add_new_book_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book('')
        assert "" not in collector.get_books_genre()

    def test_add_new_book_too_long_name(self):
        collector = BooksCollector()
        collector.add_new_book("a" * 41)
        assert "a" * 41 not in collector.get_books_genre()

    def test_add_duplicate_book(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Дюна')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    @pytest.mark.parametrize('book_name, genre', [
        ("1984", "Фантастика"),
        ("Мастер и Маргарита", "Ужасы"),
        ("Шерлок Холмс", "Детективы")
    ])
    def test_set_book_genre_valid_genre_success(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Нон-фикшн')
        assert collector.get_book_genre('1984') == ''

    def test_set_book_genre_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert collector.get_book_genre('Несуществующая книга') is None

    def test_get_book_genre_nonexistent(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Неизвестная книга') is None

    def test_add_existing_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        assert '1984' in collector.get_list_of_favorites_books()

    def test_add_nonexistent_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert 'Несуществующая книга' not in collector.get_list_of_favorites_books()

    def test_add_duplicate_book_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.add_book_in_favorites('1984')
        assert collector.get_list_of_favorites_books().count('1984') == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')
        assert '1984' not in collector.get_list_of_favorites_books()

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['1984']

    def test_get_books_genre_dict(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        assert collector.get_books_genre() == {'1984': ''}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')
        assert collector.get_books_for_children() == ['1984']

    def test_empty_favorites_list(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []