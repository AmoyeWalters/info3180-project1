"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
<<<<<<< HEAD
This file creates your application.
"""

from app import app, db
from flask import render_template, request, jsonify, send_from_directory
from app.forms import MovieForm
from app.models import Movie
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf
import os


@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})


@app.route('/api/v1/movies', methods=['POST'])
def movies():
    form = MovieForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        poster = form.poster.data

        filename = secure_filename(poster.filename)

        upload_path = app.config['UPLOAD_FOLDER']

        if not os.path.exists(upload_path):
            os.makedirs(upload_path)

        file_path = os.path.join(upload_path, filename)
        poster.save(file_path)

        new_movie = Movie(
            title=title,
            description=description,
            poster=filename
        )

        db.session.add(new_movie)
        db.session.commit()

        return jsonify({
            "message": "Movie Successfully added",
            "title": title,
            "poster": filename,
            "description": description
        }), 200

    return jsonify({
        "errors": form_errors(form)
    }), 400


@app.route('/api/v1/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()

    movie_list = []
    for movie in movies:
        movie_list.append({
            "id": movie.id,
            "title": movie.title,
            "description": movie.description,
            "poster": movie.poster
        })

    return jsonify(movies=movie_list), 200


@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


def form_errors(form):
    error_messages = []
    for field, errors in form.errors.items():
        for error in errors:
            message = f"Error in {getattr(form, field).label.text} - {error}"
            error_messages.append(message)
    return error_messages
=======
This file contains the routes for your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
from app.models import Property
from app.forms import PropertyForm
from werkzeug.utils import secure_filename
import os
from app import db

###
# Routing for your application.
###

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html', name="Properties")


###
# The functions below should be applicable to all Flask apps.
###

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
>>>>>>> 894dfe9ee2c179ee44904e2f3251831aaf09e947


@app.errorhandler(404)
def page_not_found(error):
<<<<<<< HEAD
    return render_template('404.html'), 404
=======
    return render_template('404.html'), 404


@app.route('/properties/create', methods=['GET', 'POST'])
def create_property():
    form = PropertyForm()

    if form.validate_on_submit():
        file = form.photo.data
        filename = secure_filename(file.filename)

        upload_folder = os.path.join(os.getcwd(), 'app/static/uploads')
        file.save(os.path.join(upload_folder, filename))

        new_property = Property(
            title=form.title.data,
            description=form.description.data,
            bedrooms=form.bedrooms.data,
            bathrooms=form.bathrooms.data,
            price=form.price.data,
            property_type=form.property_type.data,
            location=form.location.data,
            photo=filename
        )

        db.session.add(new_property)
        db.session.commit()

        flash('Property added successfully!', 'success')
        return redirect(url_for('properties'))

    return render_template('create_property.html', form=form)


@app.route('/properties')
def properties():
    properties = Property.query.all()
    return render_template('properties.html', properties=properties)


@app.route('/properties/<int:propertyid>')
def property_detail(propertyid):
    property = Property.query.get_or_404(propertyid)
    return render_template('property.html', property=property)
>>>>>>> 894dfe9ee2c179ee44904e2f3251831aaf09e947
