from flask import Blueprint, render_template
from website import mongo



views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("index.html")
    

