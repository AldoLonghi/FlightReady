# __init__.py is a special Python file that allows a directory to become
# a Python package so it can be accessed using the 'import' statement.

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)           # The WSGI compliant web application object
db = SQLAlchemy(app)            # Setup Flask-SQLAlchemy
manager = Manager(app)          # Setup Flask-Script

from app.startup.init_app import create_app


# The following was added so that every new connection has the command
# "PRAGMA foreign_keys = ON" executed.  Apparently there's no better way.
from sqlalchemy.engine import Engine
from sqlalchemy import event
from sqlite3 import Connection as SQLite3Connection

# Force sqllite contraint foreign keys - Must be done for each new connection!
@event.listens_for( Engine, "connect" )
def set_sqlite_pragma( dbapi_connection, connection_record ):
	"""
	Force sqllite contraint foreign keys
	"""
	if isinstance( dbapi_connection, SQLite3Connection ):
		cursor = dbapi_connection.cursor()
		cursor.execute( "PRAGMA foreign_keys = ON" )
		cursor.close()
