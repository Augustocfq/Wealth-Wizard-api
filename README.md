# Wealth Wizard API

This API allows users to input an expense explanation, such as "I spent 200 euros in shoes today", and receive the category, value, and currency of the expense in return.

## Installation

To install the dependencies of the API, run the following command in the root directory of the project:

pipenv install

This will install all the packages listed in the `Pipfile` and create a virtual environment for the project.

## Usage

To start the API, run the following command in the root directory of the project:

python flaskr/app.py

This will start the Flask app and the API will be available at `http://127.0.0.1:5000/`.

To extract the category, value, and currency of an expense explanation, send a `POST` request to the `/processexpense` endpoint with the expense explanation in the request body.
