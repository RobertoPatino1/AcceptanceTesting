print("----------ToDo List----------")


def add_task(task:str,todo_list:dict)->bool:
    if task=="":
        print("Error: Invalid task")
        return False
    elif task.capitalize() in todo_list.keys():
        print("Error: Task is already in the todo list")
        return False
    else:
        todo_list[task.capitalize()] = False
        return True
    

def list_all_tasks(todo_list:dict)->None:
    print("Tasks:")
    for task,status in todo_list.items():
        if status:
            print("- "+task+": Completed")
        else:
            print("- "+task+": Pending")


def mark_task_as_completed(task:str,todo_list:dict)->bool:
    if task.capitalize() in todo_list.keys():
        todo_list[task.capitalize()] = True
        print("Succesfully marked task as Completed")
        return True
    print("The given task was not in the todo list")
    return False


def clear_todo_list(todo_list:dict)->None:
    print("Clearing up the todo list...")
    todo_list.clear()


def remove_completed_tasks(todo_list:dict)->None:
    print("Removing all the completed tasks from the list...")
    for task,status in todo_list.items():
        if status:
            todo_list.pop(task)


def change_task_back_to_pending(task:str, todo_list:dict)->bool:
    if task.capitalize() in todo_list.keys():
        todo_list[task.capitalize()] = False
        print("Succesfully changed the task back to Pending")
        return True
    print("The given task was not in the todo list")
    return False


todo_list = {}
add_task("Buy Groceries",todo_list)
list_all_tasks(todo_list)