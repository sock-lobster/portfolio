from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea

class ContactForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    email = EmailField('Your email address:', validators=[DataRequired(), Email()])
    message = TextAreaField('Message:', widget=TextArea(), render_kw={'rows': 10},  validators=[DataRequired()])
    submit = SubmitField('Send')
