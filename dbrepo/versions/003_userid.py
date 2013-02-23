# -*- coding: utf-8 *-*
from sqlalchemy import *
from migrate import *
from blogpy.models import Base, BlogPost
from apex.models import AuthUser

user_id = Column('user_id', Integer)


def upgrade(migrate_engine):
    Base.metadata.bind = migrate_engine
    user_id.create(BlogPost.__table__)


def downgrade(migrate_engine):
    Base.metadata.bind = migrate_engine
    user_id.drop(BlogPost.__table__)
