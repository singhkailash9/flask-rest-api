# Flask REST API

This project is a simple Flask-based REST API designed to demonstrate the fundamentals of CRUD (Create, Read, Update, Delete) operations within a RESTful service architecture. It focuses on managing a collection of "cards," showcasing how to implement each of these operations using Flask. This API serves as a practical template for those interested in learning how to build and deploy RESTful APIs with Flask. Through this project, I aim to solidify my understanding of backend development principles using flask while providing a useful resource for others embarking on a similar learning journey.

## Features

- **Fetch "Hello World" Messages**: Access the `/hello` endpoint to retrieve a list of "hello world" messages. You can customize the number of messages returned by using an optional `limit` query parameter, with the default limit set to 10.

- **Serve Python Icon**: The `/python` endpoint serves a Python icon, demonstrating how static files such as images can be served through the API. This can be accessed via `GET` request to fetch the `python.png` image from the server's static folder.

- **List All Cards**: Use the `/cards` endpoint to fetch a list of all available cards in the collection.

- **Retrieve a Specific Card**: The API allows for retrieving details of a specific card by name through the `/cards/<name>` endpoint.

- **Add New Cards**: Add a new card to the collection via a POST request to the `/cards` endpoint, providing the new card's name in the request body.

- **Update Existing Cards**: Update the name of an existing card by sending a PUT request to `/cards/<name>`, including the new name in the request body.

- **Delete Cards**: Remove a card from the collection by issuing a DELETE request to `/cards/<name>`, specifying the card to be deleted.



## Installation

To run this project locally, follow these steps:

1. **Clone the repository**

```bash
    git clone https://github.com/singhkailash9/flask-rest-api.git
    cd flask-rest-api
```

2. **Set up a virtual environment** (optional, but recommended)

```bash
    python3 -m venv venv
    source venv/bin/activate
```

3. **Install dependencies**
```bash
    pip install -r requirements.txt
```
4. **Run the application**
```bash
    flask run
```
The API will be available at http://127.0.0.1:5000/.

## API Endpoints

Below are the available API endpoints for our Flask-based REST API:

### Hello World Messages

- **Endpoint**: `GET /hello`
- **Description**: Retrieves a list of "hello world" messages.
- **Query Parameters**: 
  - `limit` (optional): Integer to limit the number of returned messages. Default is 10.
- **Example**: `GET http://127.0.0.1:5000/hello?limit=5`

### Serve Python Icon

- **Endpoint**: `GET /python`
- **Description**: Serves the Python icon file.
- **Example**: `GET http://127.0.0.1:5000/python`

### Get All Cards

- **Endpoint**: `GET /cards`
- **Description**: Retrieves a list of all the cards.
- **Example**: `GET http://127.0.0.1:5000/cards`

### Get a Specific Card

- **Endpoint**: `GET /cards/<name>`
- **Description**: Retrieves a specific card by its name.
- **URL Parameters**: 
  - `name`: The name of the card to retrieve.
- **Example**: `GET http://127.0.0.1:5000/cards/yui`

### Add a New Card

- **Endpoint**: `POST /cards`
- **Description**: Adds a new card to the collection.
- **Body**: JSON object containing the `name` of the new card.
  - Example: `{"name": "new_card_name"}`
- **Example**: `POST http://127.0.0.1:5000/cards`

### Update an Existing Card

- **Endpoint**: `PUT /cards/<name>`
- **Description**: Updates the name of an existing card.
- **URL Parameters**: 
  - `name`: The current name of the card to update.
- **Body**: JSON object containing the `new_name` for the card.
  - Example: `{"new_name": "updated_card_name"}`
- **Example**: `PUT http://127.0.0.1:5000/cards/yui`

### Delete a Card

- **Endpoint**: `DELETE /cards/<name>`
- **Description**: Deletes a card from the collection.
- **URL Parameters**: 
  - `name`: The name of the card to delete.
- **Example**: `DELETE http://127.0.0.1:5000/cards/yui`


# Development
This project uses Flask for the backend. To contribute or modify the API, follow the installation steps and feel free to add new features or fix bugs.