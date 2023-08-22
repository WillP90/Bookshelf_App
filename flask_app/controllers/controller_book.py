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

# @app.route('/book/info')
# def view_book_info():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     id = {
#         'id' : session['user_id']
#     }
#     user = User.get_one_id(id)
#     return render_template('book_info.html', user = user)
# place_holder2 = 0
    # for isbn in book_isbn:
    #     isbn_url = f'https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&jscmd=data&format=json'
    #     isbn_json = requests.get(isbn_url)
    #     isbn_response = isbn_json.json()
    #     pprint(f'Dictionary keys for Book in Index {place_holder2}: {isbn_response.keys()}')
    #     place_holder2+=1
        # if statement to check for the Cover image in the Works Response
        # if 'cover'in works_response.keys():
        #     pprint(works_response['cover'])
        #     books_list[place_holder2]['cover'] = works_response['cover'][0]
        # else:
        #     pprint('no cover image')
        #     books_list[place_holder2]['cover'] = 'No Cover Image'