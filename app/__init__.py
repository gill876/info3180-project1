import requests
from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect
import os
from dotenv import load_dotenv
import datetime
#load_dotenv(verbose=True)

app = Flask(__name__)
app.config['SECRET_KEY'] = '?.jDTL_ge}PeG{v>ecXeG+64(eLc$D2c53Ku)w'
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nqiqdzogsmdwcs:ab64936bcf863c3fd2e807627bc969953c254dcc1655adf8d276c2e0d930e704@ec2-18-235-20-228.compute-1.amazonaws.com:5432/d21tjodb03ie7g'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#mail = Mail(app)
csrf = CSRFProtect(app)
csrf.init_app(app)

from app import views, models