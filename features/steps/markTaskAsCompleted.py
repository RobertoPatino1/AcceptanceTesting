from behave import given, when, then
from main import mark_task_as_completed

to_do_list = {}

@given('the to-do list contains tasks to mark one as complete')
def mark_step1_impl(context):
    global to_do_list
    to_do_list = {
        "Buy groceries": False  # False significa que no está completada
    }

@when('the user marks task "{task}" as completed')
def mark_step2_impl(context, task):
    context.success = mark_task_as_completed(task, to_do_list)

@then('the to-do list should show task "{task}" as completed')
def mark_step3_impl(context, task):
    assert to_do_list[task.capitalize()] == True, f"Task {task} was not marked as completed"
