from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
import pyodbc
import pymysql #added in case pymysql is not in the installed?

SQLALCHEMY_DATABASE_URL = '''mysql+pymysql://coe892:PublicLibrary...@automatedpubliclibrarysystem.database.windows.net/
                             AutomatedPublicLibrary?charset=utf8mb4'''  # not used
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={}, echo=True)  # not used
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # not used


AZURE_SQL_CONNECTION_STRING='''Driver={ODBC Driver 18 for SQL Server};
                              Server=tcp:automatedpubliclibrarysystem.database.windows.net,1433;
                              Database=AutomatedPublicLibrary;UID=coe892;PWD=PublicLibrary...;
                              Encrypt=yes;TrustServerCertificate=no;
                              Connection Timeout=30'''
conn = pyodbc.connect(AZURE_SQL_CONNECTION_STRING)
cursor = conn.cursor()
# user cursor.execute("SQL Query") to query the database

Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(255))
    password = Column(String(255))
    email = Column(String(255))
    full_name = Column(String(255))
    address = Column(String(255))
    phone_number = Column(String(20))

    reservations = relationship("Reservation", back_populates="user")
    borrowings = relationship("Borrowing", back_populates="user")
    recommendations = relationship("Recommendation", back_populates="user")

class Book(Base):
    __tablename__ = 'Books'

    book_id = Column(Integer, primary_key=True)
    title = Column(String(255))
    author = Column(String(255))
    publication_year = Column(Integer)
    genre = Column(String(255))
    ISBN = Column(String(20))
    available_copies = Column(Integer)
    total_copies = Column(Integer)

    reservations = relationship("Reservation", back_populates="book")
    borrowings = relationship("Borrowing", back_populates="book")
    recommendations = relationship("Recommendation", back_populates="book")

class Borrowing(Base):
    __tablename__ = 'Borrowings'

    borrowing_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'))
    book_id = Column(Integer, ForeignKey('Books.book_id'))
    borrow_date = Column(Date)
    return_date = Column(Date)
    status = Column(String(50))

    user = relationship("User", back_populates="borrowings")
    book = relationship("Book", back_populates="borrowings")

class CDs(Base):
    __tablename__ = 'CDs'

    cd_id = Column(Integer, primary_key=True)
    title = Column(String(255))
    artist = Column(String(255))
    release_year = Column(Integer)
    available_copies = Column(Integer)
    total_copies = Column(Integer)

class DVDs(Base):
    __tablename__ = 'DVDs'

    dvd_id = Column(Integer, primary_key=True)
    title = Column(String(255))
    director = Column(String(255))
    release_year = Column(Integer)
    available_copies = Column(Integer)
    total_copies = Column(Integer)

class Magazines(Base):
    __tablename__ = 'Magazines'

    magazine_id = Column(Integer, primary_key=True)
    title = Column(String(255))
    publisher = Column(String(255))
    publication_year = Column(Integer)
    available_copies = Column(Integer)
    total_copies = Column(Integer)
