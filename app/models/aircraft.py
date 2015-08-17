from flask_wtf import Form
from wtforms import FloatField, StringField, SubmitField, validators
from app import db
from user import User



class Aircraft( db.Model ):
	__tablename__ = 'aircraft'

	id = db.Column( db.Integer, primary_key=True )
	name = db.Column( db.Unicode( 50 ), nullable=False, server_default=u'', unique=True )
	registration = db.Column( db.Unicode( 50 ), nullable=False, server_default=u'' )
	# TODO: Add make/model

	hobbs = db.Column( db.Float(), nullable=False, server_default=u'0.0' )
	tach = db.Column( db.Float(), nullable=False, server_default=u'0.0' )

	users = db.relationship( 'User', secondary='users_aircraft',
	                         backref=db.backref( 'aircraft', lazy='dynamic' ) )



class UsersAircraft( db.Model ):
	__tablename__ = 'users_aircraft'

	id = db.Column( db.Integer(), primary_key=True )
	user_id = db.Column( db.Integer(), db.ForeignKey( 'users.id', ondelete='CASCADE' ) )
	aircraft_id = db.Column( db.Integer(), db.ForeignKey( 'aircraft.id', ondelete='CASCADE' ) )



class AircraftForm( Form ):
	name = StringField( 'Name', validators=[
	    validators.DataRequired( 'Name is required' )] )
	registration = StringField( 'Registration', validators=[
	    validators.DataRequired( 'Registration is required' )] )
	hobbs = FloatField( 'Hobbs', validators=[
	    validators.Optional(), validators.NumberRange( min=0.0 )] )
	tach = FloatField( 'Tach', validators=[
	    validators.Optional(), validators.NumberRange( min=0.0 )] )
	submit = SubmitField( 'Save' )
