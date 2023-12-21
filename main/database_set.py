import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from data.config import DATABASE_PRO

DATABASE_URL = DATABASE_PRO

database = databases.Database(DATABASE_URL)

Base = declarative_base()
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
