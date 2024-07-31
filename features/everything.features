# language: en

Feature: Add a task to the to-do list

    @addTaskToList
    Scenario: Add a task to the to-do list
        Given the to-do list is empty
        When the user adds a task "Buy groceries"
        Then the to-do list should contain "Buy groceries"
    
Feature: List all the tasks in the to-do list
    @listAllTasks
    Scenario: List all the tasks in the to-do list
        Given the to-do list contains tasks:
        | Task |
        | Buy groceries |
        | Pay bills |
        When the user lists all tasks
        Then the output should contain
        Tasks:
        - Buy groceries
        - Pay bills

Feature: Mark a task as completed
    @markTaskAsCompleted
    Scenario: Mark a task as completed
        Given the to-do list contains tasks:
        | Task | Status |
        | Buy groceries | Pending |
        When the user marks task "Buy groceries" as completed
        Then the to-do list should show task "Buy groceries" as completed

Feature: Clear the entire to-do list
    @clearTodoList
    Scenario: Clear the entire to-do list
        Given the to-do list contains tasks:
        | Task |
        | Buy groceries |
        | Pay bills |
        When the user clears the to-do list
        Then the to-do list should be empty