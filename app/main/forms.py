from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField("你的名字是？", validators=[DataRequired()])
    submit = SubmitField('确定')
