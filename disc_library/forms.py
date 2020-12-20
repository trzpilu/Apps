from flask_wtf import FlaskForm
from wtforms import StringField, TextField, BooleanField, IntegerField
from wtforms.validators import DataRequired

class DiscForm(FlaskForm):
    id_num = IntegerField('id_num', validators=[DataRequired()])
    author = StringField('author', validators=[DataRequired()])
    title = StringField('title', validators=[DataRequired()])
    genre = StringField('genre', validators=[DataRequired()])
    year = IntegerField('year', validators=[DataRequired()])
    description = TextField('description', validators=[DataRequired()])
    recommend = BooleanField('recommend', validators=[DataRequired()])
