from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.task_service import TaskService

task_blueprint = Blueprint('tasks', __name__)

@task_blueprint.route('/tasks/create', methods=['POST'])
def create_task():

    data = request.form
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    TaskService.create_task(name, description)
    return redirect(url_for('tasks.index'))

@task_blueprint.route('/tasks/edit/<int:task_id>', methods=['GET'])
def edit_task(task_id):
    task = TaskService.find_task(task_id)
    if not task:
        return "Tarea no encontrada", 404
    return render_template('edit_task.html', task=task)

@task_blueprint.route('/tasks/edit/<int:task_id>', methods=['POST'])
def edit_task_post(task_id):
    name = request.form.get('name')
    description = request.form.get('description')
    TaskService.edit_task(task_id, name, description)
    return redirect(url_for('tasks.index'))


@task_blueprint.route('/')
def index():
    tasks = TaskService.read_tasks()
    return render_template('index.html', tasks=tasks)