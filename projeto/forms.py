from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError

class FormCadastrar(FlaskForm):
    nome = StringField('Nome de usuário:', validators=[DataRequired()])
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    idade = StringField('Idade:', validators=[DataRequired(), Length(1, 2)])
    feedback = StringField('Feedback:', validators=[DataRequired()])
    botao_confirmar = SubmitField('Salvar')
