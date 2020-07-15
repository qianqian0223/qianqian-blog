from flask import Flask, redirect,url_for

import os 
from qianblog.controllers import blog,main
from flask_principal import identity_loaded, UserNeed, RoleNeed

from qianblog.extensions import bcrypt,openid,login_manager,principals
from flask_login import current_user
from qianblog.extensions import flask_celery
from sqlalchemy import event


from qianblog.tasks import on_reminder_save
from qianblog.models import db, User, Post, Role, Tag, Reminder
#, BrowseVolume
from qianblog.extensions import assets_env, main_js, main_css

from qianblog.extensions import  cache, flask_admin
#restful_api,debug_toolbar, 

from qianblog.controllers.admin import CustomView, CustomModelView

from qianblog.controllers import admin

def create_app(object_name):
    """Create the app instance via `Factory Method`"""

    app = Flask(__name__)
    # Set the app config 
    app.config.from_object(object_name)

    # Will be load the SQLALCHEMY_DATABASE_URL from config.py to db object
    db.init_app(app)
    # Init the Flask-Bcrypt via app object
    bcrypt.init_app(app)
    
    # Init the Flask-OpenID via app object
    openid.init_app(app)
    # Init the Flask-Login via app object
    login_manager.init_app(app)
    # Init the Flask-Prinicpal via app object
    principals.init_app(app)

    # Init the Flask-Celery-Helper via app object
    # Register the celery object into app object
    flask_celery.init_app(app)
    
    #### Init the Flask-Cache via app object
    cache.init_app(app)
    
    
    #### Init the Flask-Admin via app object
    flask_admin.init_app(app)
    # Register view function `CustomView` into Flask-Admin
    flask_admin.add_view(CustomView(name='Custom'))
    # Register view function `CustomModelView` into Flask-Admin
    models = [Role, Tag, Reminder]
    for model in models:
        flask_admin.add_view(
            CustomModelView(model, db.session, category='Models'))   
    
    # Register and define path of File System for Flask-Admin
    flask_admin.add_view(
        admin.CustomFileAdmin(
            os.path.join(os.path.dirname(__file__), 'static'),
            '/static',
            name='Static Files'))



    """Create the app instance via `Factory Method`"""

    #### Init the Flask-Assets via app object
    assets_env.init_app(app)
    assets_env.register('main_js', main_js)
    assets_env.register('main_css', main_css)


    # Will be callback on_reminder_save when insert recond into table `reminder`.
    event.listen(Reminder, 'after_insert', on_reminder_save)


    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        """Change the role via add the Need object into Role.

           Need the access the app object.
        """

        # Set the identity user object
        identity.user = current_user

        # Add the UserNeed to the identity user object
        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        # Add each role to the identity user object
        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role.name))


    # Register the Blueprint into app object
    app.register_blueprint(blog.blog_blueprint)
    app.register_blueprint(main.main_blueprint)

    return app



