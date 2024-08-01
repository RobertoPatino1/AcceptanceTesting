from behave import given,when,then
from main import add_task
to_do_list = {}
@given('the to-do list is empty')

def add_step1_impl(context):
    # Set the to-do list as an empty list
    global to_do_list
    to_do_list = {}

# Step 2: When the user adds a task "Buy groceries"
@when('the user adds a task "{task}"')
def add_step2_impl(context, task):
    # Add the task to the to-do list
    global to_do_list
    add_task(task,to_do_list)


# Step 3: Then the to-do list should contain "Buy groceries"
@then('the to-do list should contain "{task}"')
def add_step3_impl(context, task):
    # Check if the task is in the to-do list
    assert task.capitalize() in to_do_list.keys(), f'Task "{task}" not found in the to-do list'