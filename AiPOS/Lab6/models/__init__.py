from sqlalchemy import *
from sqlalchemy.orm import relationship, backref, sessionmaker

from . import base
from . import Student
from . import Course

engine = create_engine("sqlite:///./sql.db")
base.Base.metadata.create_all(engine, checkfirst=True)
Session = sessionmaker(bind=engine)
session = Session()
