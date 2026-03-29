from flask import Blueprint, request, jsonify
from models import db, Task

# Create a blueprint for our task routes
task_bp = Blueprint('tasks', __name__)

@task_bp.route('/', methods=['GET'])
def index():
    return jsonify({
        "message": "Welcome to the Simple Task Management API!",
        "endpoints": {
            "GET /tasks": "Get all tasks",
            "POST /tasks": "Create a new task",
            "PUT /tasks/<id>": "Update a task status",
            "DELETE /tasks/<id>": "Delete a task"
        }
    }), 200

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    
    # Input validation: Check if title is there and not empty string
    if not data or not data.get('title') or str(data.get('title')).strip() == '':
        return jsonify({"error": "Title is required and cannot be empty"}), 400
        
    new_task = Task(
        title=data.get('title').strip(),
        description=data.get('description', ''),
        status='pending' # Default status for a new task
    )
    
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify(new_task.to_dict()), 201

@task_bp.route('/tasks', methods=['GET'])
def get_all_tasks():
    # Adding simple pagination bonus feature
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    
    # Get tasks with pagination
    tasks_query = Task.query.paginate(page=page, per_page=limit, error_out=False)
    
    tasks_list = [task.to_dict() for task in tasks_query.items]
    
    # Return tasks and pagination info
    return jsonify({
        "tasks": tasks_list,
        "total": tasks_query.total,
        "pages": tasks_query.pages,
        "current_page": tasks_query.page
    }), 200

@task_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task_status(id):
    task = Task.query.get(id)
    
    if not task:
        return jsonify({"error": "Task not found"}), 404
        
    data = request.get_json()
    new_status = data.get('status')
    
    # Only allow valid status updates as requested
    if new_status not in ["pending", "completed"]:
        return jsonify({"error": "Invalid status. Must be 'pending' or 'completed'"}), 400
        
    task.status = new_status
    db.session.commit()
    
    return jsonify(task.to_dict()), 200

@task_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    
    if not task:
        return jsonify({"error": "Task not found"}), 404
        
    db.session.delete(task)
    db.session.commit()
    
    return jsonify({"message": "Task deleted successfully"}), 200
