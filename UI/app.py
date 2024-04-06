# for some reason database import on line 7 wasnt working, added these to fix -Mayuran
import sys
import os
import pandas as pd

from sqlalchemy import text
import pymssql

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, jsonify, request, session,  redirect, url_for
from database import engine, SessionLocal, User, Book, Item, Borrowing, CDs, DVDs, Magazines, cursor
from sqlalchemy.orm import sessionmaker
#import pymysql #CAN DELETE LATER: added this to install this library in my environment in order to get database import working (in case Mayuran's fix may not work for you) - Anthony
import requests


app = Flask(__name__)
app.secret_key = 'coe892CloudComputing'
app.config['SQLALCHEMY_DATABASE_URI'] = '''mysql+pymysql://coe892:PublicLibrary...@automatedpubliclibrarysystem.database.windows.net/
                             AutomatedPublicLibrary?charset=utf8mb4'''
Session = sessionmaker(bind=engine)



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/left-sidebar')
def left_sidebar():
    return render_template("left-sidebar.html")

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

def get_user_data(username):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Users WHERE username =" + str(username)))
        return result

# convert tuples returned from queries into string
def convertTuple(tup):
    # initialize an empty string
    string = ''
    for item in tup:
        string = string + str(item[0])
    return string

@app.route('/login/submit', methods=['post'])
def show_user():
    data = request.form
    username = data['username']
    password = data['password']
    SQL_Login_Query = '''
                        SELECT password
                        FROM Users
                        WHERE username = '{username}'
                      '''.format(username=username)
    SQL_Books_Query = '''
                        SELECT *
                        FROM Items
                        WHERE type = 'book'
                        AND available = 1
                      '''
    SQL_CDs_Query = '''
                        SELECT *
                        FROM Items
                        WHERE type = 'cd'
                        AND available = 1
                      '''
    SQL_DVDs_Query = '''
                        SELECT *
                        FROM Items
                        WHERE type = 'dvd'
                        AND available = 1
                      '''
    SQL_Magazines_Query = '''
                        SELECT *
                        FROM Items
                        WHERE type = 'magazine'
                        AND available = 1
                      '''
    result = cursor.execute(SQL_Login_Query)
    string_result = convertTuple(result)

    cursor.execute(SQL_Books_Query)
    books = cursor.fetchall()
    cursor.execute(SQL_CDs_Query)
    cds = cursor.fetchall()
    cursor.execute(SQL_DVDs_Query)
    dvds = cursor.fetchall()
    cursor.execute(SQL_Magazines_Query)
    magazines = cursor.fetchall()

    if string_result == password:
        return render_template('login_index.html', user_name=username, books=books, cds=cds, dvds=dvds, magazines=magazines) #redirect user to index page that contains library information
    else:
        return render_template('login_failed.html')


@app.route('/register')
def register():
    return render_template("register.html")


def get_max_user_id():
    SQL_Login_Query = '''
                        SELECT MAX(user_id)
                        FROM Users
                      '''
    result = cursor.execute(SQL_Login_Query)
    string_result = convertTuple(result)
    return int(string_result)
@app.route('/register/submit', methods=['post'])
def submit_register():
    data = request.form
    user_id = get_max_user_id() + 1
    username = data['username']
    password = data['password']
    email = data['email']
    address = data['address']
    fullname = data['fullname']
    phonenumber = data['phonenumber']
    SQL_Register_Query = f'''
                            INSERT INTO Users (user_id, username, password, email, full_name, address, phone_number)
                            VALUES ('{user_id}', '{username}', '{password}', '{email}', '{fullname}', '{address}', '{phonenumber}')
                         '''
    return SQL_Register_Query
    #cursor.execute(SQL_Register_Query)


@app.route('/return', methods=['GET', 'POST'])
def return_items():
    if request.method == 'POST':
        returned_item_ids = request.form.getlist('item_id')

        # Return selected items
        for item_id in returned_item_ids:
            SQL_Update_Borrowing = '''
                                    UPDATE Borrowing
                                    SET returned = 1
                                    WHERE user_id = '{user_id}'
                                    AND item_id = '{item_id}'
                                  '''.format(user_id=session.get('user_id'), item_id=item_id)
            cursor.execute(SQL_Update_Borrowing)

        # Commit the changes to the database
        cursor.commit()

        return redirect(url_for('index', return_message='Items returned successfully'))
    else:
        # Fetch borrowed items for the current user
        user_id = session.get('user_id')
        if user_id is not None:
            SQL_Borrowed_Items_Query = '''
                                        SELECT *
                                        FROM Borrowing
                                        WHERE user_id = '{user_id}'
                                        AND returned = 0
                                      '''.format(user_id=session.get('user_id'))

            cursor.execute(SQL_Borrowed_Items_Query)
        else:
            # Log an error
            print("Error: user_id is None. Cannot execute SQL query.")
        borrowed_items = cursor.fetchall()

        # Execute SQL queries to fetch available items
        SQL_Books_Query = '''
                            SELECT *
                            FROM Items
                            WHERE type = 'book'
                            AND available = 1
                          '''
        SQL_CDs_Query = '''
                            SELECT *
                            FROM Items
                            WHERE type = 'cd'
                            AND available = 1
                          '''
        SQL_DVDs_Query = '''
                            SELECT *
                            FROM Items
                            WHERE type = 'dvd'
                            AND available = 1
                          '''
        SQL_Magazines_Query = '''
                            SELECT *
                            FROM Items
                            WHERE type = 'magazine'
                            AND available = 1
                          '''

        # Fetch items from the database
        cursor.execute(SQL_Books_Query)
        books = cursor.fetchall()
        cursor.execute(SQL_CDs_Query)
        cds = cursor.fetchall()
        cursor.execute(SQL_DVDs_Query)
        dvds = cursor.fetchall()
        cursor.execute(SQL_Magazines_Query)
        magazines = cursor.fetchall()

        return render_template("return.html", borrowed_items=borrowed_items, books=books, cds=cds, dvds=dvds, magazines=magazines)

@app.route('/borrow', methods=['GET', 'POST'])
def borrow_items():
    if request.method == 'POST':
        selected_item_ids = request.form.getlist('item_id')

        # Borrow selected items
        for item_id in selected_item_ids:
            SQL_Update_Item = '''
                                UPDATE Items
                                SET available = 0
                                WHERE id = '{item_id}'
                              '''.format(item_id=item_id)
            cursor.execute(SQL_Update_Item)

            SQL_Insert_Borrowing = '''
                                    INSERT INTO Borrowing (user_id, item_id)
                                    VALUES ('{user_id}', '{item_id}')
                                  '''.format(user_id=session.get('user_id'), item_id=item_id)
            cursor.execute(SQL_Insert_Borrowing)

        # Commit the changes to the database
        cursor.commit()

        return redirect(url_for('index', borrow_message='Items borrowed successfully'))
    else:
        # Fetch available items from the database
        SQL_Available_Items_Query = '''
                                    SELECT *
                                    FROM Items
                                    WHERE available = 1
                                  '''
        cursor.execute(SQL_Available_Items_Query)
        available_items = cursor.fetchall()

        return render_template("borrow.html", available_items=available_items)


@app.route('/search')
def search():
    return render_template("search.html")

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
