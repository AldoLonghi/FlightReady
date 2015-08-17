from flask import redirect, render_template
from flask import request, url_for
from flask_user import current_user, login_required
from app import app, db
from app.models import Aircraft, AircraftForm


@app.route( '/aircraft/create', methods=['GET', 'POST'] )
@login_required
def create_aircraft_page():
	form = AircraftForm( request.form, current_user )

	# Process valid POST
	if request.method == 'POST' and form.validate():
		new_aircraft = Aircraft()
		form.populate_obj( new_aircraft )
		new_aircraft.users.append( current_user )
		db.session.add( new_aircraft )
		print( new_aircraft )
		db.session.commit()
		return redirect( url_for( 'user_page' ) )

	# Process GET or invalid POST
	return render_template( 'aircraft/create_aircraft_page.html',
	                        form=form )
