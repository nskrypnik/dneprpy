from sqlalchemy import *
from migrate import *
from apex.models import initialize_sql


def upgrade(migrate_engine):
    initialize_sql(migrate_engine, {})
