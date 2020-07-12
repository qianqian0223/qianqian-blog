from flask_wtf import Form
from wtforms import StringField, TextField
from wtforms.validators import DataRequired, Length
import re
from wtforms import ValidationError

def custom_email(form_object, field_object):
    """Define a vaildator"""

    if not re.match(r"[^@+@[^@]+\.[^@]]+", field_object.data):
        raise ValidationError('Field must be a valid email address.')



class CommentForm(Form):
    """Form vaildator for comment."""

    # Set some field(InputBox) for enter the data.
    # patam validators: setup list of validators
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=255)])

    text = TextField(u'Comment', validators=[DataRequired()])


