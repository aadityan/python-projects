from task import Task

class TaskMgr:
    def __init__(self, input_file = ''):
        self.tasks = []

    def add_task(self, title, desc, status):
        self.tasks.append(Task(self.__id_autogen(), title, desc, status))

    def delete_task(self, id):
        idx = self.__find_task(id)
        self.tasks.pop(idx)

    def update_task(self, id, new_status):
       idx = self.__find_task(id)
       self.tasks[idx].status = new_status
       
    def show_tasks(self):
        print('|------|--------------|-----------------------|------------------|')
        print('|  ID  |  TITLE       |  DESCRIPTION          |  STATUS          |')
        print('|------|--------------|-----------------------|------------------|')
        # 6, 14, 23, 19
        for task in self.tasks:
            print(f'|  {task.id:02d}  |  {self.__print(task.title, 12).ljust(12)}|  {self.__print(task.desc, 21).ljust(21)}| {self.__print(task.status, 17).ljust(17)}|')
        print('|------|--------------|-----------------------|------------------|')
        print('')

    def show_task(self, id):
        idx = self.__find_task(id)
        print(self.tasks[idx])



    # Helper / private functions
    def __print(self, text, length):
        if len(text) < length:
            return text
        return text[: length - 4] + '...'
    
    def __id_autogen(self):
        return len(self.tasks) + 1
    
    def __find_task(self, id):
        return next((i for i, task in enumerate(self.tasks) if task.id == id))
    
