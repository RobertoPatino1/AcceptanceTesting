Feature: Mark a task as completed
    @markTaskAsCompleted
    Scenario: Mark a task as completed
        Given the to-do list contains tasks to mark one as complete:
        | Task | Status |
        | Buy groceries | Pending |
        When the user marks task "Buy groceries" as completed
        Then the to-do list should show task "Buy groceries" as completed