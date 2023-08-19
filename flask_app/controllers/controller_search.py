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
    """ Get Request for Books to Open Library API"""
    # taking in search perameter from form
    title = request.form['search'].lower()
    print(title)
    session['title'] = title
    return redirect('/view/books')

@app.route('/view/books')
def view_books_search():
    # creating empty list for storing revised search
    title_search = ""
    # loop to replace all empty spaces with a + for the url search
    for i in session['title']:
        if i == " ":
            i = "+"
        title_search += i
        # pprint(i)
    # creating urls for the API call(searches book titles)(search by Works Id)
    url = f'https://openlibrary.org/search.json?title={title_search}&page=1'
    pprint(url)
    # creating a response variable to hold the json response
    json = requests.get(url)
    # storing data in a dictionary
    response = json.json()
    # this will show me the different keys in the JSON object
    pprint(response.keys())
    # printing different things to see the outcomes(Peeling that Onion Baby!!!!!)
    pprint(response['numFound'])
    pprint(response['docs'][0].keys())
    # using a temporary variable to store a number.for how many books to display from list
    temp_num = 5
    book_titles = []
    book_authors = []
    book_langs = []
    book_works_keys = []
    books_list = []
    for i in range(temp_num):
        # appending iformation to the pre set variables
        book_titles.append(response["docs"][i]["title"])
        # book_dict['title'] = response["docs"][i]["title"]
        book_authors.append(response["docs"][i]["author_name"][0])
        # book_dict['authors'] = response["docs"][i]["author_name"][0]
        book_langs.append(response["docs"][i]["language"])
        # book_dict['language'] = response["docs"][i]["language"]
        book_works_keys.append(response["docs"][i]["key"])
        books_list.append({'title' : response["docs"][i]["title"], 'authors' :response["docs"][i]["author_name"][0], 'language' : response["docs"][i]["language"]})

        # printing information about those books
    pprint(f'Book Title: {book_titles}, Author: {book_authors}, Language: {book_langs}')
    pprint(f'Book Work Keys: {book_works_keys}')
    # running loop to take Work number and fetch book info
    place_holder = 0
    for works in book_works_keys:
        works_url = f'https://openlibrary.org/{works}.json'
        works_json = requests.get(works_url)
        works_response = works_json.json()
        pprint(works_response.keys())
        if works_response['title']:
            pprint(works_response['title'])
        if 'description' in works_response.keys():
            pprint(works_response['description'])
            books_list[place_holder]['description'] = works_response['description']['value']
            place_holder+=1
        else:
            pprint('no description')
            books_list[place_holder]['description'] = 'no description'
            place_holder+=1
    pprint(f'Books List Is ---->>{books_list}')
    # make books list
    return render_template('search_book.html', books_list = books_list)