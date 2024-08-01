Feature: Change a task back to pending
    @changeTaskBackToPending
    Scenario: Change a task back to pending
        Given the to-do list contains tasks:  
        | Task | Status |  
        | Buy groceries | Pending |  
        | Walk dog | Completed |  
        When the user marks task "Walk dog" as Pending  
        Then the to-do list should show task "Walk dog" as pending 
        | Task | Status |  
        | Buy groceries | Pending | 
        | Walk dog | Pending |  