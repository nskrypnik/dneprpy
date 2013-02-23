import os
#import Image

from formalchemy import Column
from sqlalchemy import (
    Integer,
    Text,
    ForeignKey,
    String,
    DateTime,
    func
    )
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
#from apex.models import AuthUser

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

img_storage_path = os.path.join(
                            os.path.abspath(os.path.dirname(__file__)),
                            'static',
                            'uploads'
                        )


class BlogPost(Base):

    THUMB_SIZE = (200, 200)

    __tablename__ = 'blogposts'
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)
    text = Column(Text)
    image = Column(String(1024))
    date = Column(DateTime, default=func.now())

    def get_thumb(self):
        thumb_path = self.image.split('/')
        filename, ext = os.path.splitext(thumb_path[-1])
        thumb_path[-1] = ''.join([filename, '%s_%s_thumb' % self.THUMB_SIZE, ext])
        thumb_path = '/'.join(thumb_path)
        full_thumb_path = os.path.join(img_storage_path, thumb_path)
        if not os.path.exists(full_thumb_path):
            img = Image.open(os.path.join(img_storage_path, self.image))
            img.thumbnail(self.THUMB_SIZE, Image.ANTIALIAS)
            img.save(full_thumb_path)
        return "/static/uploads/%s" % thumb_path

    def __init__(self, *args, **kw):
        self.title = kw.pop('title', '')
        self.text = kw.pop('text', '')
