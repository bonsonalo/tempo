from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE= 'postgresql://postgres:password@localhost:5432/QuizApplicationYT'

 
engine= create_engine(URL_DATABASE)

sessionLocal= sessionmaker(autocommit=False, autoflush=False, bind= engine)

Base = declarative_base()  # When you call declarative_base(), SQLAlchemy creates an internal “registry” that keeps track of every table you define later by subclassing Base