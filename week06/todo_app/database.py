from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


URL_DATABSE= "postgresql://postgres:password@localhost:5432/Todo_database"

engine= create_engine(URL_DATABSE)

sessionLocal= sessionmaker(autocommit= False, autoflush=False, bind=engine)

base= declarative_base()