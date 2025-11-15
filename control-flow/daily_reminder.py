#!/usr/bin/env python3
"""
Personal Daily Reminder
This script provides customized reminders for tasks based on priority and time sensitivity.
"""

def main():
    # Prompt user for task information
    task = input("Enter your task: ").strip()
    
    # Get priority with validation loop
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in ['high', 'medium', 'low']:
            break
        else:
            print("Please enter 'high', 'medium', or 'low'")
    
    # Get time-bound status with validation loop
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in ['yes', 'no']:
            break
        else:
            print("Please enter 'yes' or 'no'")
    
    print()  # Empty line for better output formatting
    
    # Process the task using match case for priority
    match priority:
        case "high":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Please address it soon.")
        
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a medium priority task that should be completed today.")
            else:
                print(f"Note: '{task}' is a medium priority task. Try to complete it this week.")
        
        case "low":
            if time_bound == "yes":
                print(f"Note: '{task}' is a low priority task with a time constraint. Consider completing it when possible.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()