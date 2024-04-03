from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://coe892:PublicLibrarySystem...@automatedpubliclibrarysystem.database.windows.net/AutomatedPublicLibrary"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

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

class Reservation(Base):
    __tablename__ = 'Reservations'

    reservation_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'))
    book_id = Column(Integer, ForeignKey('Books.book_id'))
    reservation_date = Column(Date)
    pickup_date = Column(Date)
    status = Column(String(50))

    user = relationship("User", back_populates="reservations")
    book = relationship("Book", back_populates="reservations")

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

class Recommendation(Base):
    __tablename__ = 'Recommendations'

    recommendation_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'))
    book_id = Column(Integer, ForeignKey('Books.book_id'))
    recommendation_date = Column(Date)

    user = relationship("User", back_populates="recommendations")
    book = relationship("Book", back_populates="recommendations")

class DigitalMedia(Base):
    __tablename__ = 'DigitalMedia'

    media_id = Column(Integer, primary_key=True)
    title = Column(String(255))
    creator = Column(String(255))
    release_year = Column(Integer)
    type = Column(String(50))
    available_copies = Column(Integer)
    total_copies = Column(Integer)

class DigitalBorrowing(Base):
    __tablename__ = 'DigitalBorrowings'

    digital_borrowing_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'))
    media_id = Column(Integer, ForeignKey('DigitalMedia.media_id'))
    borrow_date = Column(Date)
    return_date = Column(Date)
    status = Column(String(50))

    user = relationship("User", back_populates="digital_borrowings")
    media = relationship("DigitalMedia", back_populates="digital_borrowings")

