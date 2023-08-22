from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    db  = "bookshelf_app_schema"

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']
        self.description = data['description']
        self.isbn = data['isbn']
        self.works_key = data['works_key']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None

    @classmethod
    def save_book(cls, data):
        query = """
                INSERT INTO books (title, author, description, isbn, works_key, user_id)
                VALUES(%(title)s, %(author)s, %(description)s, %(isbn)s, %(works_key)s, %(user_id)s);
                """
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def get_all_books_user_id(cls, data):
        query = """
        SELECT * FROM books
        WHERE user_id = %(id)s;
        """
        books = []
        results = connectToMySQL(cls.db).query_db(query, data)
        for book in results:
            books.append(cls(book))
        return books