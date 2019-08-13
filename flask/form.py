from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired(), Length (min=2, max=20)])

	email = StringField('Email', validators=[DataRequired(), Email()])

	password = PasswordField('Password', 
								validators=[DataRequired()])
	confirm_password = PasswordField('Password', 
										validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])

	username = StringField('Username', validators = [DataRequired(), Length (min=2, max=20)])


	password = PasswordField('Password', 
								validators=[DataRequired()])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')

class inputForm(FlaskForm):
	cardNumber = StringField('CardNumber', validators=[DataRequired(), Length (min=1, max=3)])

class splitForm(FlaskForm):
	firstFightStart = StringField('First Fight Start', validators=[DataRequired(), Length(6)])
	firstFightEnd = StringField('First Fight End', validators=[DataRequired(), Length(6)])
	secondFightStart = StringField('Second Fight Start', validators=[DataRequired(), Length(6)])
	secondFightEnd = StringField('Second Fight End', validators=[DataRequired(), Length(6)])
	thirdFightStart = StringField('Third Fight Start', validators=[DataRequired(), Length(6)])
	thirdFightEnd = StringField('Third Fight End', validators=[DataRequired(), Length(6)])
	fourthFightStart = StringField('Fourth Fight Start', validators=[DataRequired(), Length(6)])
	fourthFightEnd = StringField('Fourth Fight End', validators=[DataRequired(), Length(6)])
	fifthFightStart = StringField('Fifth Fight Start', validators=[DataRequired(), Length(6)])
	fifthFightEnd = StringField('Fifth Fight End', validators=[DataRequired(), Length(6)])
	filename = StringField('Filename', validators=[DataRequired()])
