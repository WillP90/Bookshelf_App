from flask_app import app
from flask import redirect, request, render_template, session
from flask_app.models.model_profile import Profile
from flask_app.models.model_user import User
from flask_app.models.model_book import Book

@app.route('/search/book')
def search_for_book():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template('search_book.html')