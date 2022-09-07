from flask import Blueprint, render_template, request
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, get_posts_by_user

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


# view for main page with all posts
@main_blueprint.route('/')
def index():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


# view for certain user's post
@main_blueprint.route('/posts/<int:post_pk>')
def post_page(post_pk):
    post = get_post_by_pk(post_pk)
    comments = get_comments_by_post_id(post_pk)

    return render_template('post.html', post=post, comments=comments)


# view for certain user's all posts
@main_blueprint.route('/users/<user_name>')
def user_posts_page(user_name):
    users_posts = get_posts_by_user(user_name)
    return render_template('user-feed.html', posts=users_posts, user_name=user_name)


