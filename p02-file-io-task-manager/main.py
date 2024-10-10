from task_mgr import TaskMgr

def main():
    
    taskMgr = TaskMgr()
    taskMgr.add_task('test task', 'Test task', 'Not started')
    taskMgr.add_task('hello', 'world', 'Pending')
    taskMgr.add_task('World', 'hello', 'In progress')
    taskMgr.add_task('LONG TITLE FOR TESTING', 'SUPER LONG DESC TO TEST HOW THIS LOOKS', 'LONG STATUS TO TEST VIZ')

    while True:
        print('\nSelect from the menu below: ')
        print(' 1. Show tasks')
        print(' 2. Detailed task view')
        print(' 3. Add task')
        print(' 4. Delete task')
        print(' 5. Update task status')
        print(' 6. Search tasks')
        print(' 7. Load tasks')
        print(' 8. Save tasks')
        print(' 9. QUIT')

        user_selection = input('--> ')

        if user_selection == '9':
            break

        calls = {
            '1': taskMgr.show_tasks,
            '2': taskMgr.show_task,
            '3': taskMgr.add_task,
            '4': taskMgr.delete_task,
            '5': taskMgr.update_task,
        }

        if int(user_selection) in range(1,9):
            if user_selection in ('2', '4'):
                calls[user_selection](int(input('Task ID: ')))
                calls['1']()
            elif user_selection == '3':
                calls[user_selection](*task_input())
                calls['1']()
            elif user_selection == '5':
                calls[user_selection](int(input('Task ID: ')), input('New Status: '))
            else:
                calls['1']()


def task_input():

    title = input('Task title: ')
    desc = input('Task description: ')
    status = input('Task status: ')

    return title, desc, status        

if __name__ == '__main__':
    main()