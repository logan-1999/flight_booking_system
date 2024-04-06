from flask import Flask, request, jsonify, abort, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy
import os

# os.system('pip install cryptography')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@db:3306/flightbooking'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


app.secret_key = 'test123'  # replace 'your_secret_key' with your actual secret key


# Define your models (User, Flights, Bookings, FlightBookings, Locations)

class Flights(db.Model):
    __tablename__ = 'Flights'
    # Assuming your Flights model is something like this
    FlightID = db.Column(db.String(50), primary_key=True)
    DepartureLocationID = db.Column(db.Integer)
    ArrivalLocationID = db.Column(db.Integer)
    DepartureDateTime = db.Column(db.DateTime)
    ArrivalDateTime = db.Column(db.DateTime)
    Price = db.Column(db.Float)
    SeatsAvailable = db.Column(db.Integer)
    Bookings = db.Column(db.Integer)
    FlightName = db.Column(db.String(50))

class Locations(db.Model):
    __tablename__ = 'Locations'
    LocationID = db.Column(db.Integer, primary_key=True)
    City = db.Column(db.String(50))
    AirportCode = db.Column(db.String(50))
    Country = db.Column(db.String(50))

class Booking(db.Model):
    __tablename__ = 'Bookings'
    BookingID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    mobile_number = db.Column(db.String(50))
    flight_id = db.Column(db.String(50))
    flight_name = db.Column(db.String(50))
    departure_location = db.Column(db.String(50))
    departure_time = db.Column(db.DateTime)
    arrival_location = db.Column(db.String(50))
    arrival_time = db.Column(db.DateTime)
    price = db.Column(db.Float)


#redirect to correct URL
@app.route("/flights/", methods=["GET"])
def redirect_external():
    return redirect("/flights", code=302)

@app.route('/flights', methods=['GET'])
def get_flights():
    try:
        flights = Flights.query.all()

        result = []
        for flight in flights:
            
            result.append({
                "FlightID": flight.FlightID,
                "DepartureLocationID": flight.DepartureLocationID,
                "ArrivalLocationID": flight.ArrivalLocationID,
                "DepartureDateTime": flight.DepartureDateTime,
                "ArrivalDateTime": flight.ArrivalDateTime,
                "Price": flight.Price,
                "SeatsAvailable": flight.SeatsAvailable,
                "Bookings": flight.Bookings,
                "FlightName": flight.FlightName
            })

        return jsonify({"status": "success", "flights": result})
    except Exception as e:
        abort(500, description=str(e))



@app.route('/', methods=['GET', 'POST'])
def welcome():
    try:
        if request.method == 'GET':
            
            return render_template('welcome.html')

    except Exception as e:
        abort(500, description=str(e)) 

@app.route('/flights/search', methods=['GET', 'POST'])
def search_flights():
    try:
        if request.method == 'GET':
            locations = Locations.query.all()
            
            return render_template('search.html', locations=locations)

    except Exception as e:
        abort(500, description=str(e)) 
     
        
@app.route('/flights/select', methods=['GET', 'POST'])
def select_flights():
    try:
        if request.method == 'GET':

            leave_from_location_id = request.args.get('leaving_from')
            going_to_location_id = request.args.get('going_to')

            # session['leave_from_location_id'] = leave_from_location_id
            # session['going_to_location_id'] = going_to_location_id

            session['leave_from_location_id'] = 2
            session['going_to_location_id'] = 3

            flights = Flights.query.filter_by(DepartureLocationID=session.get('leave_from_location_id'), ArrivalLocationID=session.get('going_to_location_id')).all()

            print(flights)

            return render_template('flights_select.html', flights=flights)
    except Exception as e:
        abort(500, description=str(e)) 

@app.route('/flights/confirm', methods=['GET', 'POST'])
def book_flights():
    try:
        if request.method == 'GET':

            selected_flight = request.args.get('selected_flight')
            session['selected_flight'] = selected_flight
            print(selected_flight)

            return render_template('flights_confirmation.html')
    except Exception as e:
        abort(500, description=str(e)) 

@app.route('/flights/booking-confirmation', methods=['GET', 'POST'])
def confirm_flights():
    try:
        if request.method == 'GET':
            flight = Flights.query.filter_by(FlightID=session.get('selected_flight')).first()
            departure_location = Locations.query.filter_by(LocationID=session.get('leave_from_location_id')).first()
            arrival_location = Locations.query.filter_by(LocationID=session.get('going_to_location_id')).first()

            session['first_name'] = request.args.get('first_name')
            session['last_name'] = request.args.get('last_name')
            session['mobile_number'] = request.args.get('mobile_number')

            # Create a new booking
            booking = Booking(
                first_name=session.get('first_name'),
                last_name=session.get('last_name'),
                mobile_number=session.get('mobile_number'),
                flight_id=flight.FlightID,
                flight_name=flight.FlightName,
                departure_location=departure_location.City,
                departure_time=flight.DepartureDateTime,
                arrival_location=arrival_location.City,
                arrival_time=flight.ArrivalDateTime,
                price=flight.Price
            )

            # Add the booking to the session
            db.session.add(booking)

            # Commit the session to write the booking to the database
            db.session.commit()

            return render_template('booking_success.html',
                                    name=session.get('first_name')+session.get('last_name'),
                                    mobile_number=session.get('mobile_number'),
                                    flight=session.get('selected_flight'),
                                    flightname = flight.FlightName,
                                    departure_location=departure_location.City,
                                    departure_time=flight.DepartureDateTime,
                                    arrival_location=arrival_location.City,
                                    arrival_time=flight.ArrivalDateTime,
                                    price=flight.Price)

        else:
            return "Invalid request method", 405
    except Exception as e:
        abort(500, description=str(e)) 



if __name__ == '__main__':
    with app.app_context():
        pass
        # db.create_all()
    app.run(debug=True, host='0.0.0.0', port='5000')


# @app.route('/user/<name>')
# def hello_user(name):
 
#     # dynamic binding of URL to function
#     if name == 'admin':
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest'
#                                 , guest=name))