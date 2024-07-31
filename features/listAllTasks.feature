Feature: List all the tasks in the to-do list
    @listAllTasks
    Scenario: List all the tasks in the to-do list
        Given the to-do list contains tasks:
        | Task |
        | Buy groceries |
        | Pay bills |
        When the user lists all tasks
        Then the output should contain
        | Tasks: |
        | - Buy groceries |
        | - Pay bills |