from flask_app import app
from flask import redirect, request, render_template, session
# from flask_app.models.model_recipe import Recipe
from flask_app.models.models_timer import Timer
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)

@app.route('/timer')
def timer_set():
    return render_template('timer.html')

