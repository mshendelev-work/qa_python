from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_one_book_only_once(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert collector.get_books_genre() == {'Дюна': ''}

    def test_add_new_book_add_book_with_valid_title_only(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир. Том первый. Чastи 1-3')
        collector.add_new_book('')
        collector.add_new_book('Преступление и наказание (перевод В. Голяницкого)')
        collector.add_new_book('Дюна')
        assert collector.get_books_genre() == {
            'Война и мир. Том первый. Чastи 1-3': '',
            'Дюна': ''
        }

    def test_set_book_genre_set_book_with_genre_fiction(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_genre() == {'Дюна': 'Фантастика'}

    def test_get_book_genre_return_genre_fiction(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_get_books_with_specific_genre_return_genre_fiction(self, book_and_genre):
        book, genre = book_and_genre
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        if genre == 'Фантастика':
            books_with_fiction_genre = collector.get_books_with_specific_genre('Фантастика')
            assert book in books_with_fiction_genre

    def test_get_books_genre_return_book_dune(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        assert collector.get_books_genre() == {'Дюна': ''}

    def test_get_books_for_children_return_genre_fiction_and_cartoon(self, book_and_genre):
        book, genre = book_and_genre
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        books_for_children = collector.get_books_for_children()
        if genre in ['Фантастика', 'Мультфильмы']:
            assert book in books_for_children
        else:
            assert book not in books_for_children

    def test_add_book_in_favorites_add_dune(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == ['Дюна']

    def test_delete_book_from_favorites_delete_dune(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.delete_book_from_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_return_dune(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Солярис')
        collector.add_book_in_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == ['Дюна']
