# Bike Theft Locator

This is a FastAPI application that helps users locate stolen and found bicycles. It fetches data from the [Bike Index API](https://bikeindex.org/documentation/api_v3) based on the provided location, duration, and other filters.

## Features

- Search for stolen or found bicycles within a specified location and duration (e.g., 6 months)
- Filter results by manufacturer
- Retrieve bike details, including manufacturer information
- Base64-encoded bike images

## Functions

- read_item: A route that takes location, distance and other optional parameters and calls to the api URL (fetch_data function). 

- fetch_data: A service which fetches the data from Bike Index API

- get_stolen_bikes_details: A utils function which converts pictures of bikes should be returned in base64 encoded format, formats the date_stolen to date time format and finally returns the bike data in JSON format.

## Installation

1. Unzip the file: bikeSearchAPI.zip

2. Navigate to the project directory: bikeSearchAPI\app

3. Create a virtual environment (optional but recommended): python -m venv .env

4. Activate the virtual environment: .env\Scripts\activate

5. Install the required dependencies: pip install -r requirements.txt

## Usage

1. Start the FastAPI server:

command>> `uvicorn app.main:app --reload`

The server will start running at `http://localhost:8000` or `http://127.0.0.1:8000`

2. Use an API client (e.g., cURL, Postman, or a web browser) to send requests to the API endpoints.

Example: `http://127.0.0.1:8000/v1/search?location=Mumbai&duration=3&manufacturer=Honda`

This will return a JSON response containing the stolen or found bicycles in the specified location (Mumbai) within the last 3 months, filtered by the manufacturer (Honda).

3. The FastAPI code can be fetched from https://t.ly/nQHLE 

Here, you will find the implementation of the code with a demo of local API call.

## API Documentation

The API documentation is available at `http://127.0.0.1:8000/docs` when the server is running.

## Testing

The project includes unit tests written using Python's `unittest` module and the `pytest` library. To run the tests, execute the following command: 
>> pytest 

## Future Scope
We can add the token and admin,  in the current code it's the commented part.
It will be helpful for authentication and accessing the API.
`bikeSearchAPI\app\dependencies.py` contains token and secret which can be used (or replaced the values) for the future scope
