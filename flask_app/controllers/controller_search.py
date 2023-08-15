from flask_app import app
import requests
from pprint import pprint
from flask import redirect, render_template, request, session
from flask_app.models.model_user import User
from flask_app.models.model_book import Book
import os

# .env file environment
header = os.environ.get('KEY')


# Helper Function
def make_request(url =f'https://www.googleapis.com/books/v1/volumes?&key={header}'):
    response = requests.get(url)
    return response.json()

@app.route('/search/book')
def search_for_book():

    """ Get Request for Books to Google books API"""
    # putting url in session for use in next and previous pages
    if not 'url' in session:
        session['url'] = (f'https://www.googleapis.com/books/v1/volumes?&key={header}')
    if 'user_id' not in session:
        return redirect('/logout')

    # saving the request to a variable for easier use using helper function
    json = make_request(session["url"])
    pprint(json)

    items_list = []
    items = json['items']
    # pprint(items)
    for i in range(len(items)):
        index = json['items'][i]['volumeInfo']
        # pprint(index)
        items_list.append(index)
        return items_list
    # pprint(items_list)



    return render_template('search_book.html')


@app.post('/process/search')
def search_name():
    pass