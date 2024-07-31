from behave import given,when,then
from main import clear_todo_list,add_task
to_do_list = {}
@given('the to-do list contains tasks')

def step_impl(context):
    # Add tasks to the todo list
    global to_do_list
    to_do_list = {}
    add_task("Buy groceries",to_do_list)
    add_task("Pay bills",to_do_list)

# Step 2: When the user clears the to-do list
@when('the user clears the to-do list')
def step_impl(context):
    global to_do_list
    clear_todo_list(to_do_list)


# Step 3: Then the to-do list should be empty
@then('the to-do list should be empty')
def step_impl(context):
    # Check if the task is in the to-do list
    assert len(to_do_list.keys())==0, f'Error clearing the todo list'