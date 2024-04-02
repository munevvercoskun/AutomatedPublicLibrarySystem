# for some reason database import on line 7 wasnt working, added these to fix -Mayuran
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request
from database import engine, SessionLocal, User, Book, Reservation, Borrowing, Recommendation, DigitalMedia, DigitalBorrowing
from sqlalchemy.orm import sessionmaker
#import pymysql #CAN DELETE LATER: added this to install this library in my environment in order to get database import working (in case Mayuran's fix may not work for you) - Anthony
import requests


app = Flask(__name__)

# Create a sessionmaker bound to the engine
Session = sessionmaker(bind=engine)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/left-sidebar')
def left_sidebar():
    return render_template("left-sidebar.html")

@app.route('/no-sidebar')
def no_sidebar():
    return render_template("no-sidebar.html")

@app.route('/right-sidebar')
def right_sidebar():
    return render_template("right-sidebar.html")

@app.route('/search')
def search():
    return render_template("search.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/return')
def return_items():
    return render_template("return.html")

@app.route('/borrow')
def borrow_items():
    
    session = Session()
    books = session.query(Book).filter(Book.available_copies > 0).all()
    session.close()
    return render_template("borrow.html", books=books)

@app.route('/searchResults', methods=['POST'])
def searchResults():
    # Assuming you want to retrieve data from the database here
    # Create a session
    session = Session()
    
    # Example: Fetch all users from the Users table
    users = session.query(User).all()
    
    # Close the session
    session.close()
    
    # Pass fetched data to the template
    return render_template("searchResults.html" , users=users)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
