from abc import ABC


class Book:
    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author


class BookRepository:
    def __init__(self, book_list: list[Book]):
        self._books = book_list

    def list_of_books(self):
        return self._books
    
    def get_book_by_id(self, id):
        return [item for item in self._books if item.id == id][0]
    

class BookService:
    def __init__(self, book_repository: BookRepository):
        self._repo = book_repository

    @property
    def get_repo(self):
        return self._repo
    
    def search_by_id(self, id):
        return self._repo.get_book_by_id(id)
    
    def all_books(self):
        return self._repo.list_of_books()