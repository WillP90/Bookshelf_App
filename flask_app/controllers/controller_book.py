from flask_app import app
from flask import redirect, request, render_template, session
from flask_app.models.model_profile import Profile
from flask_app.models.model_user import User
from flask_app.models.model_book import Book
import requests

@app.route("/user/bookshelf")
def users_bookshelf():
    if 'user_id' not in session:
        return redirect('/logout')
    id = {
        'id' : session['user_id']
    }
    user = User.get_one_id(id)
    books_list = Book.get_all_books_user_id(id)
    print(books_list)
    return render_template('my_library.html', user = user, books_list = books_list)

@app.route('/add/book/<int:isbn>')
def add_book(isbn):
    print(f'This is the ISBN----> {isbn} <----')
    isbn_url = f'https://openlibrary.org/isbn/{isbn}.json'
    response = requests.get(isbn_url)
    isbn_response = response.json()
    # print(isbn_response.keys())
    works = {
        'works_key' : isbn_response['works'][0]['key']
    }
    works_url = f"https://openlibrary.org/{works['works_key']}.json"
    response2 = requests.get(works_url)
    works_response = response2.json()
    if 'description' in works_response.keys():
        description = {
            'description' : works_response['description']['value']
        }
    else:
        description = {
            'description' : 'No Description in this search, but I am sure it is a great read!!!'
        }
    author = {
        'author' : works_response['authors'][0]['author']['key']
    }
    author_url = f"https://openlibrary.org{author['author']}.json"
    print(author_url)
    response3 = requests.get(author_url)
    author_response = response3.json()
    data = {
        'title' : isbn_response['title'],
        'author' : author_response['name'],
        'description' : description['description'],
        'isbn' : int(isbn),
        'works_key' : isbn_response['works'][0]['key'],
        'user_id' : session['user_id']
    }
    # print(data)
    Book.save_book(data)
    return redirect('/user/bookshelf')