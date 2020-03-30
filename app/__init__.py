import requests
from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
import os
from dotenv import load_dotenv
#load_dotenv(verbose=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = '?.jDTL_ge}PeG{v>ecXeG+64(eLc$D2c53Ku)w'
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/profile_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#mail = Mail(app)
csrf = CSRFProtect(app)
csrf.init_app(app)

from app import views, models