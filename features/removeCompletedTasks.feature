Feature: Remove completed tasks from the to do list
    @removeCompletedTasks
    Scenario: Remove completed tasks from the to do list
        Given the to-do list contains pending tasks:
        | Task | Status |  
        | Buy groceries | Pending |  
        | Walk dog | Completed | 
        When the user clears pending tasks 
        Then the to do list should have the following tasks as a result
        | Task | Status |  
        | Buy groceries | Pending | 