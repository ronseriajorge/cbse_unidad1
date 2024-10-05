from models.task import Task, db

class TaskRepository:

    @staticmethod
    def create_task(name, description):
        task = Task(name=name, description=description)
        db.session.add(task)
        db.session.commit()
        return task
    
    @staticmethod
    def read_tasks():
        tasks = Task.query.all()
        return tasks
    
    @staticmethod
    def get_task_by_id(task_id):
        return Task.query.get(task_id)
    
    @staticmethod
    def update_task(task_id, name, description):
        task = Task.query.get(task_id)
        if task:
            task.name = name
            task.description = description
            db.session.commit()    

    @staticmethod
    def delete_task(task_id):
        task = Task.query.get(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()