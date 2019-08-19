from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
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
	cardNumberSelect = SelectField('CardNumberSelect', choices=[('ppv','PPV'), ('espn', 'ESPN'), ('fightNight', 'Fight Night')])

class splitForm(FlaskForm):
	firstFightStart = StringField('firstFightStart', validators=[DataRequired(), Length(min=6, max=6, message='Time must be 6 numbers')])
	firstFightEnd = StringField('firstFightEnd', validators=[DataRequired(), Length(min=6, max=6, message='Time must be 6 numbers')])
	secondFightStart = StringField('secondFightStart', validators=[DataRequired(), Length(min=6, max=6, message='Time must be 6 numbers')])
	secondFightEnd = StringField('secondFightEnd', validators=[DataRequired(), Length(min=6, max=6, message='Time must be 6 numbers')])
	thirdFightStart = StringField('thirdFightStart', validators=[DataRequired(), Length(min=6, max=6, message='Time must be 6 numbers')])
	thirdFightEnd = StringField('thirdFightEnd', validators=[DataRequired(), Length(min=6, max=6, message='Time must be 6 numbers')])
	fourthFightStart = StringField('fourthFightStart', validators=[DataRequired(), Length(min=6, max=6, message='Time must be 6 numbers')])
	fourthFightEnd = StringField('fourthFightEnd', validators=[DataRequired(), Length(min=6, max=6, message='Time must be 6 numbers')])
	fifthFightStart = StringField('fifthFightStart', validators=[DataRequired(), Length(min=6, max=6, message='Time must be 6 numbers')])
	fifthFightEnd = StringField('fifthFightEnd', validators=[DataRequired(), Length(min=6, max=6, message='Time must be 6 numbers')])
	sixthFightStart = StringField('sixthFightStart', validators=[DataRequired(), Length(min=6, max=6, message='Time must be 6 numbers')])
	sixthFightEnd = StringField('sixthFightEnd', validators=[DataRequired(), Length(min=6, max=6, message='Time must be 6 numbers')])

	filename = StringField('filename', validators=[DataRequired()])
