from repositories.task_repository import TaskRepository

class TaskService:

    @staticmethod
    def create_task(name, description):
        return TaskRepository.create_task(name, description)
    
    @staticmethod
    def read_tasks():
        return TaskRepository.read_tasks()
    
    @staticmethod
    def find_task(task_id):
        return TaskRepository.get_task_by_id(task_id)   
     
    @staticmethod
    def edit_task(task_id, name, description):
        TaskRepository.update_task(task_id, name, description)