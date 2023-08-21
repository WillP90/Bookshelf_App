from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    db  = "bookshelf_app_schema"

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']
        self.description = data['description']
        self.isbn = data['isbn']
        self.language = data['language']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None

    @classmethod
    def save_book(cls, data):
        query = """
                INSRET INTO books (title, author, description, isbn, language, user_id)
                VALUES(%(title)s, %(author)s, %(description)s, %(isbn)s, %(language)s, %(user_id)s);
                """
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def get_all_books_user_id(cls, id):
        query = """
        SELECT * FROM books
        WHERE user_id = %(user_id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, id)
        if results:
            books = cls(results[0])
            return books
        return False