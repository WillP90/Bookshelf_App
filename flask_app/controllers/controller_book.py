from flask_app import app
from flask import redirect, request, render_template, session
from flask_app.models.model_profile import Profile
from flask_app.models.model_user import User
from flask_app.models.model_book import Book

@app.route("/user/bookshelf")
def users_bookshelf():
    if 'user_id' not in session:
        return redirect('/logout')
    id = {
        'id' : session['user_id']
    }
    user = User.get_one_id(id)
    books = Book.get_all_books_user_id(session['user_id'])
    return render_template('my_library.html', user = user, books = books)

@app.route('/book/info')
def view_book_info():
    if 'user_id' not in session:
        return redirect('/logout')
    id = {
        'id' : session['user_id']
    }
    user = User.get_one_id(id)
    return render_template('book_info.html', user = user)