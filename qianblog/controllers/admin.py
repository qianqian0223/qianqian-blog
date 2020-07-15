from flask_admin import BaseView, expose

from flask_admin.contrib.sqla import ModelView
from qianblog.forms import CKTextAreaField

from flask_login import login_required, current_user
from qianblog.extensions import admin_permission


from flask_admin.contrib.fileadmin import FileAdmin



class CustomView(BaseView):
    """View function of Flask-Admin for Custom page."""

    @expose('/')
    @login_required
    @admin_permission.require(http_exception=403)
    def index(self):
        return self.render('admin/custom.html')

    @expose('/second_page')
    @login_required
    @admin_permission.require(http_exception=403)
    def second_page(self):
        return self.render('admin/second_page.html')




class CustomModelView(ModelView):
    """View function of Flask-Admin for Models page."""
    def is_accessible(self):
        """Setup the access permission for CustomModelView."""

        # callable function `User.is_authenticated()`.
        # FIXME(JMilkFan): Using function is_authenticated()
        return current_user.is_authenticated and\
            admin_permission.can()

    

class PostView(CustomModelView):
    """View function of Flask-Admin for Post create/edit Page includedin Models page"""

    # Using the CKTextAreaField to replace the Field name is `test`
    form_overrides = dict(text=CKTextAreaField)

    # Using Search box
    column_searchable_list = ('text', 'title')

    # Using Add Filter box
    column_filters = ('publish_date',)

    # Custom the template for PostView
    # Using js Editor of CKeditor
    create_template = 'admin/post_edit.html'
    edit_template = 'admin/post_edit.html'

class CustomFileAdmin(FileAdmin):
    """File System admin."""
    def is_accessible(self):
        """Setup the access permission for CustomFileAdmin."""

        # callable function `User.is_authenticated()`.
        return current_user.is_authenticated and\
            admin_permission.can()

