from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://coe892:PublicLibrarySystem...@coe892:1433/AutomatedPublicLibrary"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
