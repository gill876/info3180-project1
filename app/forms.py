from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email

class Profile(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    gender = SelectField(u'Gender', choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    biography = TextAreaField('Biography', validators=[DataRequired()])
    profile_img = FileField('Profile Picture', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'jpeg', 'Images only!'])
    ])