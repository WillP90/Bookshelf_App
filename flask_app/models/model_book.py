from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    db  = "bookshelf_app_schema"

    def __init__(self, data):
        pass