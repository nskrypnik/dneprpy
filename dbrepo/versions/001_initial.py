from sqlalchemy import *
from migrate import *
from blogpy.models import Base

class BlogPost(Base):

    __table_args__ = {'extend_existing': True}

    __tablename__ = 'blogposts'
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)
    text = Column(Text)
    image = Column(String(1024))
    date = Column(DateTime, default=func.now())


def upgrade(migrate_engine):
    Base.metadata.bind = migrate_engine
    BlogPost.__table__.create()


def downgrade(migrate_engine):
    Base.metadata.bind = migrate_engine
    BlogPost.__table__.drop()
