from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL= "postgresql://postgress:password@localhost:5432/jwt_practice"

engine= create_engine(DATABASE_URL)

SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()