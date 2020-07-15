from flask_admin import BaseView, expose

from flask_admin.contrib.sqla import ModelView
from qianblog.forms import CKTextAreaField

class CustomView(BaseView):
    """View function of Flask-Admin for Custom page."""

    @expose('/')
    def index(self):
        return self.render('admin/custom.html')

    @expose('/second_page')
    def second_page(self):
        return self.render('admin/second_page.html')




class CustomModelView(ModelView):
    """View function of Flask-Admin for Models page."""
    pass

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
