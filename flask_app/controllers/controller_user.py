from flask_app import app
from flask import redirect, request, render_template, session
# from flask_app.models.model_recipe import Recipe
from flask_app.models.model_user import User
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('log_reg.html')

@app.route('/user/process', methods=['POST'])
def register_new_user():
    valid = User.user_validation(request.form)
    if not valid:
        return redirect('/')
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : bcrypt.generate_password_hash(request.form['password'])
    }
    user = User.save_new_user(data)
    session['user_id'] = user
    return redirect('/profile')

@app.route('/profile')
def show_users_profile():

    if 'user_id' not in session:
        return redirect('/logout')
    id = {
        'id' : session['user_id']
    }
    # all_recipes = Recipe.get_all_recipes() all_recipes = all_recipes
    user = User.get_one_id(id)
    return render_template('profile.html', user = user)

@app.route('/login/user', methods=['POST'])
def user_profile_login():
    data = {
        'email' : request.form['email']
    }
    user = User.get_user_email(data)
    if not user:
        flash("Invalid Email/Password", 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password", 'login')
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/profile')