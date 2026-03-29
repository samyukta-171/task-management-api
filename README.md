# Task Management REST API

This project is a simple Task Management REST API built using Flask and SQLite. It allows users to create, view, update, and delete tasks. The goal of this project is to understand how REST APIs work along with database integration.

---

## Features

* Create a new task
* View all tasks
* Update task status (pending / completed)
* Delete a task
* Input validation
* Pagination support

---

## Technologies Used

* Python
* Flask
* SQLite
* SQLAlchemy

---

## Project Structure

```
task-api/
│
├── app.py
├── models.py
├── routes.py
├── config.py
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/task-management-api.git
cd task-management-api
```

---

### 2. Create virtual environment (optional but recommended)

```
python -m venv venv
venv\Scripts\activate   (Windows)
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Run the application

```
python app.py
```

Server will start at:

```
http://127.0.0.1:5000/
```

---

## API Endpoints

### 1. Create Task

```
POST /tasks
```

Request Body:

```
{
  "title": "Learn Flask",
  "description": "Practice building APIs"
}
```

---

### 2. Get All Tasks

```
GET /tasks
```

With pagination:

```
GET /tasks?page=1&limit=5
```

---

### 3. Update Task Status

```
PUT /tasks/<id>
```

Request Body:

```
{
  "status": "completed"
}
```

---

### 4. Delete Task

```
DELETE /tasks/<id>
```

---

## Sample Curl Commands

### Create Task

```
curl -X POST http://127.0.0.1:5000/tasks \
-H "Content-Type: application/json" \
-d "{\"title\":\"Test Task\",\"description\":\"Demo\"}"
```

---

### Get Tasks

```
curl http://127.0.0.1:5000/tasks
```

---

### Update Task

```
curl -X PUT http://127.0.0.1:5000/tasks/1 \
-H "Content-Type: application/json" \
-d "{\"status\":\"completed\"}"
```

---

### Delete Task

```
curl -X DELETE http://127.0.0.1:5000/tasks/1
```

---

## Error Handling

* Returns 400 for invalid input
* Returns 404 if task not found

---

