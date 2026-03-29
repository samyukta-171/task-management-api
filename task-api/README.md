# Task Management API

This is a simple REST API for managing tasks. I built this for tracking tasks with a title, description, and status. It uses Flask and a local SQLite database using SQLAlchemy.

## Features
- Add a new task
- View all tasks (with basic pagination)
- Update a task's status (pending/completed)
- Delete a task

## How to run the project

1. **Install requirements:**
   Make sure you have Python installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the server:**
   Start the application by running:
   ```bash
   python app.py
   ```
   The API will run locally at `http://127.0.0.1:5000`. The database file `database.db` will be created automatically in the same folder.

## API Endpoints

### 1. Create a Task
* **URL:** `/tasks`
* **Method:** `POST`
* **Data:**
  ```json
  {
      "title": "Buy groceries",
      "description": "Milk, eggs, and bread"
  }
  ```

### 2. Get All Tasks
* **URL:** `/tasks`
* **Method:** `GET`
* **Query Params:** `?page=1&limit=5` (optional, for pagination)

### 3. Update Task Status
* **URL:** `/tasks/<id>`
* **Method:** `PUT`
* **Data:**
  ```json
  {
      "status": "completed"
  }
  ```

### 4. Delete Task
* **URL:** `/tasks/<id>`
* **Method:** `DELETE`

## Example curl commands for testing

**Create a task:**
```bash
curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d "{\"title\":\"Finish homework\", \"description\":\"Math and Physics\"}"
```

**Get all tasks:**
```bash
curl http://127.0.0.1:5000/tasks
```
Or with pagination:
```bash
curl "http://127.0.0.1:5000/tasks?page=1&limit=2"
```

**Update a task:**
```bash
curl -X PUT http://127.0.0.1:5000/tasks/1 -H "Content-Type: application/json" -d "{\"status\":\"completed\"}"
```

**Delete a task:**
```bash
curl -X DELETE http://127.0.0.1:5000/tasks/1
```
