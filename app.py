from apiflask import APIFlask, abort
from db import Task, session
from schema import TaskOutputSchema, TaskCreateSchema, TaskUpdateSchema
from flask import jsonify

app = APIFlask(__name__)

@app.get('/')
def home():
    return {'message' : 'Hello World'}

@app.get('/tasks')
def get_all_task():
    posts = session.query(Task).all() 
    
    schema = TaskOutputSchema()
    result = schema.dump(posts, many=True)

    return jsonify(result)

@app.post('/tasks')
@app.input(TaskCreateSchema)
@app.output(TaskOutputSchema)
def create_tasks(data):
    content = data.get('content')
    
    new_task = Task(content=content)
    session.add(new_task)
    session.commit()

    return new_task, 201


@app.get('/tasks/<int:task_id>')
@app.output(TaskOutputSchema)
def get_task_by_id(task_id):
    task = session.query(Task).filter_by(id=task_id).first()

    if task is not None:
        return task, 200

    abort(404, 'You do not have any task here')    

@app.put('/tasks/<int:task_id>')    
@app.input(TaskUpdateSchema)
@app.output(TaskOutputSchema)
def update_task(task_id, data):
    content = data.get('content')
    is_completed = data.get('is_completed')

    task_to_update = session.query(Task).filter_by(id=task_id).first()
    task_to_update.content = content
    task_to_update.is_completed = is_completed

    session.commit()

    return task_to_update

@app.delete('/tasks/<int:task_id>')
def delete_task(task_id):
    task_to_delete = session.query(Task).filter_by(id=task_id).first()

    session.delete(task_to_delete)

    session.commit()

    return {'message' : 'Task deleted'}, 204

