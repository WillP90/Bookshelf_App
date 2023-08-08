from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import User

class Book:
    db  = "bookshelf_app_schema"

    def __init__(self, data):
        pass