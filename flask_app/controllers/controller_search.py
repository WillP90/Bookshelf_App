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
    title = request.form['search']
    # print(title)
    title_search = ""
    for i in title:
        if i == " ":
            i = "+"
        title_search += i
        # pprint(i)
    # creating url for the API call(searches book titles)
    url = f'https://openlibrary.org/search.json?q={title_search}'
    pprint(url)
    # creating a response variable to hold the json response
    json = requests.get(url)
    response = json.json()
    pprint(response)

    # url = f'https://www.googleapis.com/books/v1/volumes?q={title_search}+intitle+:keyes&key={header}'
    # pprint(url)
    # response = requests.get(url)
    # pprint(response.json()['items'][0]['volumeInfo']['title'])
    """ Get Request for Books to Open Library API"""

    # putting url in session for use in next and previous pages
    # if not 'url' in session:
    #     session['url'] = (f'https://www.googleapis.com/books/v1/volumes?q={title_search}+intitle:keyes&key={header}')
    # if 'user_id' not in session:
    #     return redirect('/logout')
    # response = requests.get(url =f'https://www.googleapis.com/books/v1/volumes?q={title_search}intitle+:keyes&key={header}')

    # saving the request to a variable for easier use using helper function
    # pprint(response.json())
    # items_list = []
    # items = response.json()
    # # pprint(items)
    # for i in range(len(items)):
    #     index = response.json()['items'][i]['volumeInfo']['title']
    #     pprint(index)
    #     items_list.append(index)
    #     pprint(items_list)
    # return items_list

    # for i in items_list:
    #     session['book'] = items_list
        # session['book'] = {
        #     'title': i['title'],
        #     # 'image': i['image'],
        # }
        # session['book_list'].append(session['book'])
        # pprint(session['books_list'][0])
        # print(session['book'])
        # print(i)

    return redirect('/view/books')

@app.route('/view/books')
def view_books_search():
    # books_list = session['book_list']
    return render_template('search_book.html')