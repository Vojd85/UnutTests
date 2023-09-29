import unittest
from unittest.mock import Mock
from book_service import BookService

class TestBookService(unittest.TestCase):
    def setUp(self):
        self.book_service = BookService(Mock())

    def test_book_list(self):
        self.book_service.all_books()
        self.book_service.get_repo.list_of_books.assert_called()

    def test_search_by_id(self):
        self.book_service.search_by_id(10)
        self.book_service.get_repo.get_book_by_id.assert_called_once_with(10)


if __name__ == '__main__':
    unittest.main(verbosity=2)