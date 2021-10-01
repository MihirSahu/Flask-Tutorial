from flask import Flask, render_template #render_template is for using html files
from flask_sqlalchemy import SQLAlchemy #sql integration with flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db' #use app.config() to make flask recognize the database, and create database file
db = SQLAlchemy(app) #create a database. Any classes created inside flask app for sql will be considered 'models' for this database

#While developing export variable FLASK_APP=pythonFileName and FLASK_DEBUG=1
