import json

from flask import jsonify


def get_posts_all():
    """Returns the list of posts"""
    with open ('data/posts.json', 'r', encoding='utf-8') as file:
        list_of_posts = json.load(file)
        return list_of_posts


def get_comments_all():
    """Returns the list of comments"""
    with open('data/comments.json', 'r', encoding='utf-8') as file:
        list_of_posts = json.load(file)
        return list_of_posts


def get_posts_by_user(user_name):
    """returns certain user's posts """
    posts = get_posts_all()
    user_posts = []

    for post in posts:

        if post['poster_name'] == user_name:
            user_posts.append(post)

    return user_posts


def get_post_by_pk(post_pk):
    """returns post with certain pk"""
    posts = get_posts_all()

    for post in posts:
        if post["pk"] == post_pk:
            return post


def get_comments_by_post_id(post_id):
    """returns comments for certain post with pk"""
    comments = get_comments_all()
    posts_comments = []

    for comm in comments:
        if comm['post_id'] == post_id:
            posts_comments.append(comm)

    return posts_comments


def search_for_posts(query):
    """returns posts with certain word """
    posts = get_posts_all()
    suitable_posts = []

    for post in posts:
        if query.lower().strip() in post['content'].lower():
            suitable_posts.append(post)

    return suitable_posts


