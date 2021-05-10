from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from .config import Config

class DecryptionForm(FlaskForm):
    cyphertext = StringField('Cyphertext (c)', validators=[DataRequired()])
    exponent = StringField('Public Exponent (e)', validators=[DataRequired()])
    public_key = StringField('Prime Product (n)', validators=[DataRequired()])
