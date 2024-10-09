from task import Task

class TaskMgr:
    def __init__(self):
        self.tasks = []

    def add_task(self, id, title, desc, status):
        self.tasks.append(Task(id, title, desc, status))

    def show_tasks(self):
        print('|------|--------------|-----------------------|------------------|')
        print('|  ID  |  TITLE       |  DESCRIPTION          |  STATUS          |')
        print('|------|--------------|-----------------------|------------------|')
        # 6, 14, 23, 18
        for task in self.tasks:
            print(f'|  {task.id:02d}  |  {self.__print(task.title, 12).ljust(12)}|  {self.__print(task.desc, 21).ljust(21)}| {self.__print(task.status, 17).ljust(17)}|')

    def __print(self, text, length):
        if len(text) < length:
            return text
        return text[: length - 4] + '...'
    
