from flask_app import app
import requests
from pprint import pprint
from flask import redirect, render_template, request, session
from flask_app.models.model_user import User
from flask_app.models.model_book import Book



# Helper Function
def make_request(url =f'https://www.googleapis.com/books/v1/volumes?q=search+terms:keyes&key={KEY}'):
    response = requests.get(url)
    return response.json()

@app.route('/search/book')
def search_for_book():
    # response = requests.get("https://www.googleapis.com/books/v1/volumes?q=search+terms")
    # print(str(response.status_code).center(20, "-"))

    """ Get Request for Books to Google books API"""
    # putting url in session for use in next and previous pages
    if not 'url' in session:
        session['url'] = 'https://www.googleapis.com/books/v1/volumes?q=search+termskeyes&key=AIzaSyBCxm0VWW3yC_yjqDCfkqIcj-bPozm3YNw'
    if 'user_id' not in session:
        return redirect('/logout')

    # saving the request to a variable for easier use using helper function
    json = make_request(session["url"])
    pprint(json)


    return render_template('search_book.html')


@app.post('/process/search')
def search_name():
    pass