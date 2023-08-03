from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Profile:
    db  = "bookshelf_app_schema"

    def __init__(self, data):
        self.id = data['id']
        self.genre = data['genre']
        self.location = data['location']
        self.info = data['info']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None

    @classmethod
    def save_user_profile(cls, data):
        query = """
                INSERT INTO profiles (genre, location, info, user_id)
                VALUES (%(genre)s, %(location)s, %(info)s, %(user_id)s)"""
        result = connectToMySQL(cls.db).query_db(query, data)
        return result