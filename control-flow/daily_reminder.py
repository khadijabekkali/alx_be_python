# daily_reminder.py
# Single task reminder using conditional statements, match-case, and loops

def main():
    # Prompt for task details
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Match-case for priority
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' has an undefined priority"

    # Modify reminder if time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    # Print the reminder
    print("\nReminder:", reminder)

    # Optional congratulatory message using a loop
    for i in range(1):
        print("\nWell done on completing this project! Let the world hear about this milestone achieved.\n🚀 Click here to tweet! 🚀")

if __name__ == "__main__":
    main()
