import pandas as pd
import numpy as np

# import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
# from sqlalchemy import text

from flask import (
    Flask,
    # request,
    # redirect,
    # url_for,
    # flash,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

app = Flask(__name__)

#################################################
# Database Setup
#################################################

# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root123@127.0.0.1:3306/books_db'

#connection to My_SQL
engine = create_engine('mysql://root:root123@127.0.0.1:3306/read_db')
#engine = create_engine("sqlite:///indicators_project.sqlite")
session = Session(engine)


# db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
isbn_data=Base.classes.isbn_data
author_data=Base.classes.author_data
publ_data=Base.classes.publ_data


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")



@app.route("/api/booksearch/<title>", methods=['GET'] )
def booksearch(title):
    """Return book(s) based on title search. Limit to top 10."""

    sel=[isbn_data.ISBN, 
        isbn_data.bookTitle,
        isbn_data.book_average_rating,
        author_data.bookAuthor,
        author_data.author_gender,
        author_data.birthplace,
        publ_data.yearOfPublication,
        publ_data.publisher]

    results=session.query(*sel).join(author_data, author_data.ISBN==isbn_data.ISBN).join(publ_data, publ_data.ISBN==isbn_data.ISBN).filter(isbn_data.bookTitle==title).all()
            

    data_all=[]
    for item in results:
        data={}
        data['isbnNumber']=item[0]
        data['bookTitle']=item[1]
        data['author_rating']=float(item[2])
        data['author']=item[3]
        data['author_gender']=item[4]
        data['birthplace']=item[5]
        data['year_publication']=item[6]
        data['publisher']=item[7]
        data_all.append(data)
    return jsonify (data_all)


@app.route('/api/authorsearch/<author>', methods =['GET'])
def authorsearch(author):
    sel=[author_data.bookAuthor,
            author_data.author_gender, 
            author_data.birthplace,
            isbn_data.bookTitle,
            isbn_data.book_average_rating]

    results=session.query(*sel).join(author_data, author_data.ISBN==isbn_data.ISBN).filter(author_data.bookAuthor==author).distinct()

    books=[]
    data={}

    for item in results:
        books.append(item[3])
        
    data['authorName']=results[0][0]
    data['gender']=results[0][1]
    data['birthplace']=results[0][2]
    data['author_rating']=float(results[0][4])
    data['books']=books
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)
