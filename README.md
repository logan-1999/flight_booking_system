# Flight Booking Application

This is a Flask application for booking flights. It uses SQLAlchemy to interact with a MySQL database.

## Setup

1. Clone the repository.
2. run `docker compose up -d`
3. It will setup your db and app infra
4. navigate to "localhost:5001"

## Note
- This is 2 Tier Application, meaning 
- UI and Application Logic are in same layer, and a DB in the backened
- I have hardcoded flight id as arrival for 2 and desitination for 3, because we don't have enough data yet in the db.

## Models

The application has three models:

- `Flights`: Represents a flight. Fields include `FlightID`, `DepartureLocationID`, `ArrivalLocationID`, `DepartureDateTime`, `ArrivalDateTime`, `Price`, `SeatsAvailable`, `Bookings`, and `FlightName`.

- `Locations`: Represents a location. Fields include `LocationID`, `City`, `AirportCode`, and `Country`.

- `Booking`: Represents a booking. Fields include `BookingID`.



# Database Design

The application uses a MySQL database with three tables: `Flights`, `Locations`, and `Bookings`.

## Flights

The `Flights` table represents a flight. It has the following fields:

- `FlightID`: The primary key of the table.
- `DepartureLocationID`: A foreign key that references the `Locations` table.
- `ArrivalLocationID`: A foreign key that references the `Locations` table.
- `DepartureDateTime`: The date and time of departure.
- `ArrivalDateTime`: The date and time of arrival.
- `Price`: The price of the flight.
- `SeatsAvailable`: The number of seats available on the flight.
- `Bookings`: The number of bookings made for the flight.
- `FlightName`: The name of the flight.

## Locations

The `Locations` table represents a location. It has the following fields:

- `LocationID`: The primary key of the table.
- `City`: The city of the location.
- `AirportCode`: The airport code of the location.
- `Country`: The country of the location.

## Bookings

The `Bookings` table represents a booking. It has the following fields:

- `BookingID`: The primary key of the table.
- `FlightID`: A foreign key that references the `Flights` table.
- `UserID`: The ID of the user who made the booking.
- `BookingDate`: The date the booking was made.


Please note that this is a simplified representation of the database design. Depending on the requirements of your application, you might need to add more tables or fields, or change the relationships between the tables.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
