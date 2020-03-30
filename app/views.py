"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from app import app
from flask import render_template, request, redirect, url_for, flash
from .forms import Profile
from app.models import ProfileDB
from . import db
from werkzeug.utils import secure_filename


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    """Render profile's page."""
    profile = Profile()
    if request.method == 'POST' and profile.validate_on_submit():
        fname = profile.fname.data
        lname = profile.lname.data
        email = profile.email.data
        location = profile.location.data
        gender = profile.gender.data
        biography = profile.biography.data
        profile_img = profile.profile_img.data
        filename = secure_filename(profile_img.filename)
        
        person = ProfileDB(fname, lname, email, location, gender, biography, filename)
        db.session.add(person)
        db.session.commit()
        profile_img.save(os.path.join(
            app.config['UPLOAD_FOLDER'], filename
        ))
            
        flash('Profile added!', 'success')
        return redirect(url_for('home'))
    flash_errors(profile)
    return render_template('profile.html', form=profile)


###
# The functions below should be applicable to all Flask apps.
###

def format_date_joined():
    now = datetime.datetime.now() # today's date
    date_joined = datetime.date(2019, 2, 7) # a specific date 
    ## Format the date to return only month and year date
    return date_joined.strftime("%B, %Y")

# @app.route('/<file_name>.txt')
# def send_text_file(file_name):
#     """Send your static text file."""
#     file_dot_text = file_name + '.txt'
#     return app.send_static_file(file_dot_text)


# @app.after_request
# def add_header(response):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also tell the browser not to cache the rendered page. If we wanted
#     to we could change max-age to 600 seconds which would be 10 minutes.
#     """
#     response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
#     response.headers['Cache-Control'] = 'public, max-age=0'
#     return response

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")