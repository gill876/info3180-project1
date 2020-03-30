from . import db
import datetime

class ProfileDB(db.Model):
    __tablename__ = 'profiles'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(150))
    gender = db.Column(db.String(10))
    biography = db.Column(db.String(500))
    filename = db.Column(db.String(250))
    date_created = db.Column(db.DateTime, default=datetime.date.today())

    def __init__(self, fname, lname, email, location, gender, biography, filename):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.location = location
        self.gender = gender
        self.biography = biography
        self.filename = filename
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.email)