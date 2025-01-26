class BooksRepository:
    def __init__(self):
        self.books = [
            {
                "id": 1,
                "title": "To Kill a Mockingbird",
                "author": "Harper Lee",
                "year": 1960,
                "total_pages": 336,
                "genre": "Fiction",
            },
            {
                "id": 2,
                "title": "1984",
                "author": "George Orwell",
                "year": 1949,
                "total_pages": 328,
                "genre": "Dystopian",
            },
            {
                "id": 3,
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "year": 1925,
                "total_pages": 180,
                "genre": "Classic",
            },
            {
                "id": 4,
                "title": "The Lord of the Rings",
                "author": "J.R.R. Tolkien",
                "year": 1954,
                "total_pages": 1178,
                "genre": "Fantasy",
            },
            {
                "id": 5,
                "title": "The Catcher in the Rye",
                "author": "J.D. Salinger",
                "year": 1951,
                "total_pages": 224,
                "genre": "Coming-of-age",
            },
        ]
        self.next_id = 1

    def get_books(self, offset: int = 0, limit: int = 10):
        return self.books[offset:offset + limit]

    def get_book(self, book_id: int):
        return next((book for book in self.books if book["id"] == book_id), None)

    def create_book(self, title: str, author: str, year: int, total_pages: int, genre: str):
        book = {
            "id": self.next_id,
            "title": title,
            "author": author,
            "year": year,
            "total_pages": total_pages,
            "genre": genre,
        }
        self.books.append(book)
        self.next_id += 1
        return book
