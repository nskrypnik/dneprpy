# -*- coding: utf-8 *-*

from pyramid_rpc.jsonrpc import jsonrpc_method
from .models import DBSession, BlogPost


@jsonrpc_method(endpoint="api")
def get_posts_after(request, post_id):
    last_post = DBSession().query(BlogPost).get(post_id)
    _pquery = DBSession().query(BlogPost)\
        .filter(BlogPost.date < last_post.date)\
        .filter(BlogPost.id != last_post.id)\
        .order_by(BlogPost.date.desc()).limit(10)

    def post2json(post):
        jpost = dict(
                id=post.id,
                title=post.title,
                text=post.text,
                author='',
                thumb='',
            )
        if post.image:
            jpost['thumb'] = post.get_thumb()
        if post.user:
            jpost['author'] = post.user.login
        return jpost

    return [post2json(post) for post in _pquery.all()]


@jsonrpc_method(endpoint="api", permission="authenticated")
def add_post(request, title, text):
    pass


@jsonrpc_method(endpoint="api", permission="authenticated")
def get_posts(request, count, post_id):
    pass

