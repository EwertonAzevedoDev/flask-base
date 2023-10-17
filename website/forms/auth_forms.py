from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_wtf import FlaskForm


'''
class Ubs(FlaskForm):
    ubs = SelectField('Unidade de Saúde', choices=[(x['ubs'], x['ubs']) for x in mongo.ubss.find()])
    submit = SubmitField("Selecionar")
'''

'''
class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Nome de Login"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=160)], render_kw={"placeholder": "Senha"})
    submit = SubmitField("Registrar")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        
        if existing_user_username:
            raise ValidationError(
                "Este usuário já existe. Por favor escolha outro."
            )
'''

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Nome de Login"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=160)], render_kw={"placeholder": "Senha"})
    submit = SubmitField("Entrar")
    remember = BooleanField("Lembrar meu login e senha neste dispositivo")