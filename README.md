# RESTful API for working with PostGIS Database

### This project is an implementation of a RESTful API that allows working with a PostgreSQL database with PostGIS extension.
The API enables performing operations on places, including retrieving a list of places, creating new places, updating place information, deleting places, and finding the nearest place to a specified point.

## Requirements
Before getting started with the project, make sure you have the following components installed on your computer:

- PostgreSQL with PostGIS extension
- Django DRF
- OSGeo4W (installation and configuration instructions can be found at: https://docs.djangoproject.com/en/4.2/ref/contrib/gis/install/#postgis)


## Project Setup
To set up the project, follow these steps:

- Clone this repository to your local machine.
- Start PostgreSQL with the PostGIS extension.
- Create a database and a table using the following SQL command:
```sql
Copy code
CREATE DATABASE <database_name>;
\c <database_name>;
CREATE EXTENSION postgis;
CREATE TABLE places (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    geom GEOMETRY(Point, 4326)
);
```
 - Optionally, populate the places table with some sample data.

## Django setup:

In the terminal, navigate to the project directory.
Run the following command to install the dependencies:
```shell
pip install -r requirements.txt
``` 


 - In the settings.py file (for Django), configure the connection parameters for the PostgreSQL database:
    Create a .env file to store your environment variables:
    ```
        DJANGO_SECRET_KEY=DJANGO_SECRET_KEY
        POSTGRES_DB=POSTGRES_DB
        POSTGRES_USER=POSTGRES_USER
        POSTGRES_PASSWORD=POSTGRES_PASSWORD
        POSTGRES_HOST=POSTGRES_HOST
        POSTGRES_PORT=POSTGRES_PORT
    ```
Start the server according to the instructions for the Django framework.

## Using the API
### The API provides access to the following endpoints:

 - GET /places - Get a list of all places.
 - POST /places - Create a new place.
 - GET /places/{id} - Get information about a specific place by its identifier.
 - PUT /places/{id} - Update information about a specific place by its identifier.
 - DELETE /places/{id} - Delete a specific place by its identifier.
 - GET /places/nearest - Find the nearest place to a specified point.


## API Documentation

### API documentation generated using drf_yasg is available within the project at the following endpoint:
 - http://127.0.0.1:8000/api/gis/swagger/
