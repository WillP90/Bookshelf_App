from flask_app import app
from flask import redirect, request, render_template, session
from flask_app.models.model_user import User
from flask_app.models.model_profile import Profile



@app.route('/edit/profile/<int:user_id>')
def edit_page(user_id):
    profile = Profile.get_one_profile_id(user_id)
    return render_template('edit_profile.html', user_id = user_id, profile = profile)


@app.post('/edit/profile/process')
def process_profile():
    data ={
        "genre" : request.form['genre'],
        "location" : request.form['location'],
        "info" : request.form['info'],
        "user_id" : request.form['user_id']
    }
    if Profile.get_one_profile_id(data) == False:
        profile = Profile.save_user_profile(data)
        return redirect('/profile')
    profile = Profile.update_profile(data)
    return redirect('/profile')
