class TaskManager:
    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, title):
        if title is None or not title.strip():
            raise ValueError("Task title cannot be empty.")
        if len(title.strip()) > 100:
            raise ValueError("Task title is too long (max 100 characters).")
        task = {"id": self._next_id, "title": title.strip(), "done": False}
        self.tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self):
        return list(self.tasks)

    def complete_task(self, task_id):
        pass

    def delete_task(self, task_id):
        pass
