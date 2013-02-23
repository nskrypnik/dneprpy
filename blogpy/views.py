from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from sqlalchemy.exc import DBAPIError

from formalchemy import FieldSet
from formalchemy.ext.fsblob import FileFieldRenderer

from .models import (
    DBSession,
    BlogPost,
    img_storage_path,
    )


def blogpost_form_factory(model, session=None, request=None):
    form = FieldSet(model, session=session, request=request)
    exclude = [form.user_id, form.user, form.date]
    form.configure(exclude=exclude,
            options=[
                form.text.textarea(),
                form.image.with_renderer(
                    FileFieldRenderer.new(
                            storage_path=img_storage_path,
                        )
                    )
                ]
        )
    return form


@view_config(route_name='home', renderer='index.mako')
def my_view(request):
    query = DBSession.query(BlogPost).order_by(BlogPost.date.desc()).limit(10)
    posts = query.all()
    return dict(posts=posts)


@view_config(route_name='addpost', renderer='addpost.mako',
    request_method='GET', permission="authenticated")
def addpost_page(request):
    postform = blogpost_form_factory(BlogPost, session=DBSession())
    return dict(postform=postform)


@view_config(route_name='addpost', renderer='addpost.mako',
    request_method='POST', permission="authenticated")
def addpost(request):
    user = request.user.users[0]
    postform = blogpost_form_factory(BlogPost, session=DBSession(),
        request=request)
    postform.model.user_id = user.id
    if postform.validate():
        postform.sync()
        return HTTPFound(request.route_url('home'))
    return {}
