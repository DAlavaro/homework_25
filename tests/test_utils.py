import pytest
from utils import *


# tests for functions from utils.py
def test_get_posts_all():

    assert len(get_posts_all()) != 0, 'Длина списка не должна равняться 0'
    assert type(get_posts_all()) == list, 'Тип возвращаемого файла должен быть list'


def test_get_comments_all():

    assert len(get_comments_all()) != 0, 'Длина списка не должна равняться 0'
    assert type(get_comments_all()) == list, 'Тип возвращаемого файла должен быть list'


def test_get_posts_by_user():

    assert len(get_posts_by_user('leo')) == 2, 'Количество возвращаемых постов не совпадает с фактич. кол - вом'
    assert len(get_posts_by_user('ololo')) == 0, 'Количество возвращаемых постов несуществующего юзера != 0'
    assert type(get_posts_by_user('leo')[0]) == dict, 'Элементом списка является не словарь'


def test_get_post_by_pk():

    assert get_post_by_pk(-1) == None, 'Возрвращается пост с несущестующим pk'
    assert type(get_post_by_pk(1)) == dict, 'Возвращается не словарь'


def test_get_comments_by_post_id():
    assert len(get_comments_by_post_id(1)) == 4, 'возвращается неверное количество комментариев'
    assert len(get_comments_by_post_id(-1)) == 0, 'возвращаются комментарии несуществующего поста'
    assert len(get_comments_by_post_id(-1)) == 0, 'Тип возвращаемого файла должен быть list'


def test_search_for_post():
    assert type(search_for_posts("я")) == list, 'возвращается не список'
