from repositories.task_repository import TaskRepository

class TaskService:

    @staticmethod
    def create_task(name, description):
        return TaskRepository.create_task(name, description)
    
    @staticmethod
    def read_tasks():
        return TaskRepository.read_tasks()