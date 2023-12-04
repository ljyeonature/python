''' app/crud/views.py '''

from flask import Blueprint, render_template

crud = Blueprint('crud', __name__, static_folder='static', template_folder='templates')

# http://127.0.0.1:5000/crud
@crud.route('/')
def index():
    return render_template('crud/index.html')
    # crud/templates + crud/index.html