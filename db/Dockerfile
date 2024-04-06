# Stage 1: Run the Python script
FROM python:3.8 AS builder
WORKDIR /app
COPY ./generate_dummy_data.py .
RUN python generate_dummy_data.py

# Stage 2: Create the MySQL container
FROM mysql:8.0
COPY --from=builder /app/flight_data.sql /docker-entrypoint-initdb.d/flight_data.sql