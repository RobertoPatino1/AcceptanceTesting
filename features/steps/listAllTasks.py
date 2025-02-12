from behave import given, when, then
from io import StringIO
import sys

from main import list_all_tasks

to_do_list = {}

@given('the to-do list contains tasks to list')
def list_step1_impl(context):
    global to_do_list
    to_do_list = {
        "Buy groceries": False,  
        "Pay bills": False       
    }

@when('the user lists all tasks')
def list_step2_impl(context):
    context.stdout = StringIO()
    sys.stdout = context.stdout

    list_all_tasks(to_do_list)

    sys.stdout = sys.__stdout__

@then('the output should contain')
def list_step3_impl(context):
    expected_output = "Tasks:\n- Buy groceries: Pending\n- Pay bills: Pending\n"
    actual_output = context.stdout.getvalue()

    assert actual_output == expected_output, f"Expected:\n{expected_output}\nBut got:\n{actual_output}"
