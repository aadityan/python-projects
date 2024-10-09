from task_mgr import TaskMgr

def main():
    
    taskMgr = TaskMgr()
    taskMgr.add_task(1, 'test task', 'Test task', 'Not started')
    taskMgr.add_task(2, 'hello', 'world', 'Pending')
    taskMgr.add_task(3, 'World', 'hello', 'In progress')
    taskMgr.add_task(4, 'LONG TITLE FOR TESTING', 'SUPER LONG DESC TO TEST HOW THIS LOOKS', 'LONG STATUS TO TEST VIZ')

    taskMgr.show_tasks()

if __name__ == '__main__':
    main()