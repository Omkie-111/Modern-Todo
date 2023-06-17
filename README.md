# AlgoBulls To-Do List App

This is a simple To-Do List application built using Django and Django Rest Framework.

## Requirements

- Python 3.8+
- Django 3.1+
- Django Rest Framework 3.1+

## Installation

1. Clone the repository:
  git clone <repository-url>

2. Change into the project directory:
  
cd todolist
  
3. Create a virtual environment:
 
python -m venv venv
  
4. Activate the virtual environment:

- On macOS and Linux:

  ```
  source venv/bin/activate
  ```

- On Windows:

  ```
  venv\Scripts\activate
  ```

5. Install the dependencies:

pip install -r requirements.txt
  
6. Apply the database migrations:

python manage.py migrate
  
7. Run the development server:

python manage.py runserver
  
The app will be accessible at `http://localhost:8000/`.

## Usage

- Access the Django admin interface at `http://localhost:8000/admin/` to manage the To-Do List app models.

- Use the following API endpoints to interact with the app:

- **CREATE a todo item**: `POST /api/tasks/`
- **READ one todo item**: `GET /api/tasks/{task_id}/`
- **READ all todo items**: `GET /api/tasks/`
- **UPDATE a todo item**: `PUT /api/tasks/{task_id}/`
- **DELETE a todo item**: `DELETE /api/tasks/{task_id}/`

- Basic authentication is enabled for all API endpoints. Provide the username and password as part of the request.

## Postman Collection

A Postman collection is provided for testing the API endpoints. You can import the collection into Postman and use it to interact with the app.

- Postman Collection: [Link to Postman Collection]()



