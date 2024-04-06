-- FlightID (PK)
-- FlightName
-- DepartureLocationID (FK)
-- ArrivalLocationID (FK)
-- DepartureDateTime
-- ArrivalDateTime
-- Price
-- SeatsAvailable
-- Bookings

-- BookingID (PK)
-- FlightID (FK)
-- UserID (FK, optional, assuming you have a user management system)
-- NumberOfPassengers
-- Status (e.g., Confirmed, Cancelled)
-- BookingDateTime
-- Locations

-- LocationID (PK)
-- City
-- AirportCode
-- Country

USE flightbooking;
#Location Table
CREATE TABLE Locations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY,
    City VARCHAR(255) NOT NULL,
    AirportCode VARCHAR(10) NOT NULL,
    Country VARCHAR(255) NOT NULL
);

INSERT INTO Locations 
	(City, AirportCode, Country) 
VALUES 
	('New York', 'JFK', 'USA'), 
	('Los Angeles', 'LAX', 'USA'), 
    ('London', 'LHR', 'UK'), 
    ('Tokyo', 'HND', 'Japan'),
    ('Paris', 'CDG', 'France'), 
    ('Dubai', 'DXB', 'UAE'), 
    ('Sydney', 'SYD', 'Australia'), (
    'Singapore', 'SIN', 'Singapore'), 
    ('Berlin', 'BER', 'Germany'), 
    ('Toronto', 'YYZ', 'Canada');





#Flight Table
CREATE TABLE Flights (
    FlightID INT AUTO_INCREMENT PRIMARY KEY,
    FLightName VARCHAR(255) NOT NULL,
    DepartureLocationID INT,
    ArrivalLocationID INT,
    DepartureDateTime DATETIME NOT NULL,
    ArrivalDateTime DATETIME NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    SeatsAvailable INT NOT NULL,
    Bookings INT,
    FOREIGN KEY (DepartureLocationID) REFERENCES Locations(LocationID),
    FOREIGN KEY (ArrivalLocationID) REFERENCES Locations(LocationID)
);



#user Table
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Email VARCHAR(255) NOT NULL UNIQUE,
    PasswordHash VARCHAR(255) NOT NULL
);


#bookings Table
CREATE TABLE Bookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    mobile_number VARCHAR(50),
    flight_id VARCHAR(50),
    flight_name VARCHAR(50),
    departure_location VARCHAR(50),
    departure_time DATETIME,
    arrival_location VARCHAR(50),
    arrival_time DATETIME,
    price FLOAT
);
