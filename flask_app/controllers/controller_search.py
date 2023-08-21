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
        # pprint(i) //// Use to see the variables items to make sure its working
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
    # setting up empty lists to store response values
    book_titles = []
    book_authors = []
    book_langs = []
    book_works_keys = []
    book_isbn = []
    books_list = []
    # for loop to run through the top searches coming back/// can be changed by temp_num above
    for i in range(temp_num):
        pprint(response['docs'][i].keys())
        # appending iformation to the pre set variables for printing in the f string below.
        book_titles.append(response["docs"][i]["title"])
        book_authors.append(response["docs"][i]["author_name"][0])
        book_langs.append(response["docs"][i]["language"])
        book_works_keys.append(response["docs"][i]["key"])
        book_isbn.append(response["docs"][i]["isbn"][0])
        # appending information as a data structure into a empty list to use
        books_list.append({'title' : response["docs"][i]["title"], 'authors' :response["docs"][i]["author_name"][0], 'language' : response["docs"][i]["language"]})

        # printing information about those books
    pprint(f'Book Title: {book_titles}, Author: {book_authors}, Language: {book_langs}')
    pprint(f'Book Work Keys: {book_works_keys}')
    pprint(f'ISBN: {book_isbn}')

    # Running Loop to take Work number and fetch book info
    # Creating a placeholder number to use as an index indicator for the loop
    place_holder = 0
    for works in book_works_keys:
        # running a query for each of the books that returned a Works Key
        works_url = f'https://openlibrary.org/{works}.json'
        # setting the request to a variable
        works_json = requests.get(works_url)
        # setting the javascript object notation to the request
        works_response = works_json.json()
        # printing the keys to make sure they are there
        pprint(f"Dictionary key for Book in Index {place_holder}: {works_response.keys()}")
        # statement to get the title from the Works Request instead of the Search Request since we need the info there to
        if works_response['title']:
            # printing it to make sure its there while we are iterating and that its changing
            pprint(works_response['title'])
        # statement to check if there is a description key in the call because not all the Works Requests have a Description
        if 'description' in works_response.keys():
            # printing the result if there is a result pulled
            pprint(works_response['description'])
            # instead of appening to the list, you gotta add the key name and item into the data set thats at that index
            books_list[place_holder]['description'] = works_response['description']['value']
            place_holder+=1
        # if there is no description, then it will make one for it that says no description
        else:
            pprint('no description')
            books_list[place_holder]['description'] = 'No Description'
            place_holder+=1

    place_holder2 = 0
    for isbn in book_isbn:
        isbn_url = f'https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=data&format=json'
        isbn_json = requests.get(isbn_url)
        isbn_response = isbn_json.json()
        pprint(f'Dictionary keys for Book in Index {place_holder2}: {isbn_response.keys()}')
        place_holder2+=1
        # if statement to check for the Cover image in the Works Response
        # if 'cover'in works_response.keys():
        #     pprint(works_response['cover'])
        #     books_list[place_holder2]['cover'] = works_response['cover'][0]
        # else:
        #     pprint('no cover image')
        #     books_list[place_holder2]['cover'] = 'No Cover Image'


    pprint(f'Books List Is ---->>{books_list}')
    # make books list
    return render_template('search_book.html', books_list = books_list)