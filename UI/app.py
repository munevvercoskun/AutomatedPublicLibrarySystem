# for some reason database import on line 7 wasnt working, added these to fix -Mayuran
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, session, redirect, url_for
from database import engine, SessionLocal, User, Book, Reservation, Borrowing, Recommendation, DigitalMedia, DigitalBorrowing, CDs, DVDs, Magazines
from sqlalchemy.orm import sessionmaker
#import pymysql #CAN DELETE LATER: added this to install this library in my environment in order to get database import working (in case Mayuran's fix may not work for you) - Anthony
import requests


app = Flask(__name__)
app.secret_key = 'coe892CloudComputing'
Session = sessionmaker(bind=engine)

@app.route('/')
def index():
    if 'user_id' in session:
        user_id = session['user_id']
        session = Session()
        user = session.query(User).filter_by(user_id=user_id).first()
        user_name = user.full_name  # Accessing the user's full name
        borrowed_items = session.query(Borrowing).filter_by(user_id=user_id).all()
        session.close()
        return render_template("index.html", user_name=user_name, borrowed_items=borrowed_items)
    else:
        # If the user is not logged in, redirect to the login page
        return redirect(url_for('login'))

@app.route('/left-sidebar')
def left_sidebar():
    return render_template("left-sidebar.html")

@app.route('/search')
def search():
    return render_template("search.html")

@app.route('/login', methods=['GET', "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        session = Session()
        user = session.query(User).filter_by(username=username, password=password).first()
        session.close()
        
        if user:
            session['user_id'] = user.user_id
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/return')
def return_items():
    user_id = 1  
    session = Session()
    borrowed_items = session.query(Borrowing).filter_by(user_id=user_id).all()
    session.close()
    return render_template("return.html", borrowed_items=borrowed_items)

@app.route('/borrow')
def borrow_items():
    
    session = Session()
    books = session.query(Book).all()
    cds = session.query(CDs).all()
    dvds = session.query(DVDs).all()
    magazines = session.query(Magazines).all()
    session.close()
    return render_template("borrow.html", books=books, cds=cds, dvds=dvds, magazines=magazines)

@app.route('/searchResults', methods=['POST'])
def searchResults():
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
