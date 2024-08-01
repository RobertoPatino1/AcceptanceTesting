from behave import given, when, then
from main import remove_completed_tasks

to_do_list = {}

@given('the to-do list contains pending tasks')
def remove_completed_task_step1_impl(context):
    global to_do_list
    to_do_list = {
        "Buy groceries": False,  
        "Walk dog": True       
    }

@when('the user clears pending tasks')
def remove_completed_task_step2_impl(context):
    remove_completed_tasks(to_do_list)

@then('the to do list should have the following tasks as a result')
def remove_completed_task_step3_impl(context):
    expected_to_do_list = {
        "Buy groceries": False
    }
    assert to_do_list == expected_to_do_list, f"Expected:\n{expected_to_do_list}\nBut got:\n{to_do_list}"
