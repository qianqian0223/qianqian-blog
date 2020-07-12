from flask import Flask, redirect,url_for

from qianblog.models import db
from qianblog.controllers import blog,main

from qianblog.extensions import bcrypt

def create_app(object_name):
    """Create the app instance via `Factory Method`"""

    app = Flask(__name__)
    # Set the app config 
    app.config.from_object(object_name)

    # Will be load the SQLALCHEMY_DATABASE_URL from config.py to db object
    db.init_app(app)
    # Init the Flask-Bcrypt via app object
    bcrypt.init_app(app)


    # Register the Blueprint into app object
    app.register_blueprint(blog.blog_blueprint)
    app.register_blueprint(main.main_blueprint)

    return app



