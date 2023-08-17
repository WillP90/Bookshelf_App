from flask_app import app
import requests
from pprint import pprint
from flask import redirect, render_template, request, session
from flask_app.models.model_user import User
from flask_app.models.model_book import Book
import os

# .env file environment
header = os.environ.get('KEY')

@app.route('/search/book')
def display_book_search():
    return render_template('search_book.html')


@app.route('/book/info')
def display_book_info():
    pass



@app.post('/process/search/title')
def search_book_title():
    title_search = request.form['search']
    """ Get Request for Books to Google books API"""
    # Helper Function
    def make_request_title(url =f'https://www.googleapis.com/books/v1/volumes?q={title_search}intitle+:keyes&key={header}'):
        response = requests.get(url)
        return response.json()

    # putting url in session for use in next and previous pages
    if not 'url' in session:
        session['url'] = (f'https://www.googleapis.com/books/v1/volumes?q={title_search}+intitle:keyes&key={header}')
    if 'user_id' not in session:
        return redirect('/logout')

    # saving the request to a variable for easier use using helper function
    json = make_request_title(session["url"])
    pprint(json)
    items_list = []
    items = json['items']
    # pprint(items)
    for i in range(len(items)):
        index = json['items'][i]['volumeInfo']
        # pprint(index)
        items_list.append(index)
        pprint(items_list)
        return items_list
    for i in items_list:
        session['book'] = {
            'title': i[0]['title'],
            # 'image': i['image'],
        }
        session['book_list'].append(session['book'])
        pprint(session['books_list'][0])

    return redirect('/view/books')

@app.route('/view/books')
def view_books_search():
    books_list = session['book_list']
    return render_template('search_book.html', books_list = books_list)