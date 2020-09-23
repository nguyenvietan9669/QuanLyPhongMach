from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:@localhost/quanlyphongmach?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.secret_key = "\x98\xccx\r\r57\xfb\xccj!\xdf\xbf/\x10"

db = SQLAlchemy(app = app)

admin = Admin(app=app,name='QUẢN LÝ PHÒNG MẠCH',template_mode="bootstrap3")
login  = LoginManager(app=app)