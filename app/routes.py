from app import app
from flask import render_template, redirect, url_for, g, request, jsonify, make_response
import sqlite3

DATABASE = '' # path to database file goes here

app.config['app_name'] = 'HelloWorld'


# sqlite db helpers
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def home():
	return render_template("home.html")