# FastAPI CRUD Todo Application

This is a simple CRUD (Create, Read, Update, Delete) application for managing todos, built using FastAPI.

## Features

- Get all todos
- Get a single todo by ID
- Create a new todo
- Update an existing todo
- Delete a todo

## Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn (for running the application)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fastapi-crud.git
   cd fastapi-crud
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install fastapi uvicorn
   ```

## Usage

1. Run the application:
   ```
   uvicorn main:app --reload
   ```

2. Open your browser and go to `http://localhost:8000/docs` to see the Swagger UI documentation and test the API endpoints.

## API Endpoints

- `GET /`: Root endpoint, returns a "Hello World" message
- `GET /todos`: Get all todos
- `GET /todos/{todo_id}`: Get a single todo by ID
- `POST /todos`: Create a new todo
- `PUT /todos/{todo_id}`: Update an existing todo
- `DELETE /todos/{todo_id}`: Delete a todo

## Project Structure

- `main.py`: Contains the FastAPI application and route handlers
- `models.py`: Defines the Todo model using Pydantic

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
