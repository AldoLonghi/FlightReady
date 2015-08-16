# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from flask import render_template
from flask_user import current_user, login_required, roles_accepted

from app import app
from app.models import Aircraft, UsersAircraft


# The Home page is accessible to anyone
@app.route( '/' )
def home_page():
	return render_template( 'pages/home_page.html' )

# The User page is accessible to authenticated users (users that have logged in)
@app.route( '/user' )
@login_required             # Limits access to authenticated users
def user_page():
	my_aircraft = Aircraft.query.join( UsersAircraft ).filter_by( user_id = current_user.id ).all()
	return render_template( 'pages/user_page.html', my_aircraft=my_aircraft )

# The Admin page is accessible to users with the 'admin' role
@app.route( '/admin' )
@roles_accepted( 'admin' )    # Limits access to users with the 'admin' role
def admin_page():
	return render_template( 'pages/admin_page.html' )
