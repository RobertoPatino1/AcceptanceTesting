from behave import given, when, then
from main import change_task_back_to_pending

to_do_list = {}

@given('the to-do list contains tasks to change completed ones back to pending')
def change_task_back_to_pending_step1_impl(context):
    global to_do_list
    to_do_list = {
        "Buy groceries": False,  # False significa que está pendiente
        "Walk dog": True         # True significa que está completada
    }

@when('the user marks task "{task}" as Pending')
def change_task_back_to_pending_step2_impl(context, task):
    context.success = change_task_back_to_pending(task, to_do_list)

@then('the to-do list should show task "{task}" as pending')
def change_task_back_to_pending_step3_impl(context, task):
    task = task.capitalize()
    assert to_do_list[task] == False, f"Task {task} was not changed back to pending"
    expected_to_do_list = {
        "Buy groceries": False,
        "Walk dog": False
    }
    assert to_do_list == expected_to_do_list, f"Expected:\n{expected_to_do_list}\nBut got:\n{to_do_list}"
