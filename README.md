# qa_python
Метод test_add_new_book_add_one_book_only_once проверяет, что метод add_new_book побавляет одну книгу только один раз.

Метод test_add_new_book_add_book_with_valid_title_only проверяет, что метод add_new_book добавляет только книги с 
валидным названием.

Метод test_set_book_genre_set_book_with_genre_fiction проверяет, что метод set_book_genre верно устанавливает  
жанр книге.

Метод test_get_book_genre_return_genre_fiction проверяет, что метод get_book_genre верно возвращает жанр книги по её 
имени.

Метод test_get_books_with_specific_genre_return_genre_fiction проверяет, что метод get_books_with_specific_genre выводит
книги с определённым жанром.

Метод test_get_books_genre_return_book_dune проверяет, что метод get_books_genre успешно возвращает словарь
books_genre.

Метод test_get_books_for_children_return_genre_fiction_and_cartoon проверяет, что метод get_books_for_children 
возвращает книги без возрастного ограничения.

Метод test_add_book_in_favorites_add_dune проверяет, что метод add_book_in_favorites успешно добавляет книгу в 
избранное.

Метод test_delete_book_from_favorites_delete_dune проверяет, что метод delete_book_from_favorites успешно удаляет 
книгу из избранного.

Метод test_get_list_of_favorites_books_return_dune проверяет, что метод get_list_of_favorites_books верно возвращает 
весь список избранных книг.
