from flask import Flask, Blueprint, render_template, request
from utils import search_for_posts

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


# view for user's search
@search_blueprint.route('/search/')
def search_page():
    s = request.args.get('s')
    suitable_posts = search_for_posts(s)

    return render_template('search.html', posts=suitable_posts)
