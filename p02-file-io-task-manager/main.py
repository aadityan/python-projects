from task_mgr import TaskMgr

def main():
    
    taskMgr = TaskMgr()
    taskMgr.add_task('test task', 'Test task', 'Not started')
    taskMgr.add_task('hello', 'world', 'Pending')
    taskMgr.add_task('World', 'hello', 'In progress')
    taskMgr.add_task('LONG TITLE FOR TESTING', 'SUPER LONG DESC TO TEST HOW THIS LOOKS', 'LONG STATUS TO TEST VIZ')

    taskMgr.show_tasks()

    taskMgr.update_task(1, 'pending')
    taskMgr.show_tasks()

    taskMgr.delete_task(1)
    taskMgr.show_tasks()

    taskMgr.delete_task(3)
    taskMgr.show_tasks()
    taskMgr.show_task(2)

if __name__ == '__main__':
    main()