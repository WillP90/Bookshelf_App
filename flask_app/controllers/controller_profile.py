from flask_app import app
from flask import redirect, request, render_template, session
from flask_app.models.model_user import User

@app.route('/edit/profile/<int:user_id>')
def edit_page(user_id):
    return render_template('edit_profile.html', user_id = user_id)