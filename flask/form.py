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
	firstFightStart = StringField('firstFightStart', validators=[DataRequired(), Length(6)])
	firstFightEnd = StringField('firstFightEnd', validators=[DataRequired(), Length(6)])
	secondFightStart = StringField('secondFightStart', validators=[DataRequired(), Length(6)])
	secondFightEnd = StringField('secondFightEnd', validators=[DataRequired(), Length(6)])
	thirdFightStart = StringField('thirdFightStart', validators=[DataRequired(), Length(6)])
	thirdFightEnd = StringField('thirdFightEnd', validators=[DataRequired(), Length(6)])
	fourthFightStart = StringField('fourthFightStart', validators=[DataRequired(), Length(6)])
	fourthFightEnd = StringField('fourthFightEnd', validators=[DataRequired(), Length(6)])
	fifthFightStart = StringField('fifthFightStart', validators=[DataRequired(), Length(6)])
	fifthFightEnd = StringField('fifthFightEnd', validators=[DataRequired(), Length(6)])
	filename = StringField('filename', validators=[DataRequired()])
