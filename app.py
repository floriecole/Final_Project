import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import text

from flask import (
    Flask,
    request,
    redirect,
    url_for,
    flash,
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

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root123@127.0.0.1:3306/books_db'

#connection to My_SQL
engine = create_engine('mysql://root:root123@127.0.0.1:3306/books_db', pool_pre_ping=True)
#engine = create_engine("sqlite:///indicators_project.sqlite")
session = Session(engine)


db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# Save references to each table



@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")



# @app.route("/countries")
# def countries():
#     """Return a list of country names."""

#     # Use Pandas to perform the sql query
#     stmt = db.session.query(gdpind).statement
#     df = pd.read_sql_query(stmt, db.session.bind)
#     # Return a list of unique country names in the first column
#     return jsonify(list(df['country'].unique()))








if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
