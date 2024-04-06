import random
from datetime import datetime, timedelta
import os

f = open('flight_data.sql', 'w')

for i in range(1, 51):
    flight_id = i
    flight_name = f'Flight {i}'
    departure_location_id = random.randint(1, 5)
    arrival_location_id = random.randint(1, 5)
    while departure_location_id == arrival_location_id:
        arrival_location_id = random.randint(1, 5)
    departure_date = datetime.now() + timedelta(days=random.randint(1, 30))
    arrival_date = departure_date + timedelta(hours=random.randint(1, 5))
    price = round(random.uniform(50.0, 500.0), 2)
    seats_available = random.randint(20, 100)
    bookings = random.randint(0, seats_available)


    print(f"USE flightbooking; INSERT INTO Flights (FlightID, FlightName, DepartureLocationID, ArrivalLocationID, DepartureDateTime, ArrivalDateTime, Price, SeatsAvailable, Bookings) VALUES ({flight_id}, '{flight_name}', {departure_location_id}, {arrival_location_id}, '{departure_date.strftime('%Y-%m-%d %H:%M:%S')}', '{arrival_date.strftime('%Y-%m-%d %H:%M:%S')}', {price}, {seats_available}, {bookings});", file=f)