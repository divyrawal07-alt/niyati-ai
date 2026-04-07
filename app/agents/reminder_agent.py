def set_reminders(schedule):
    reminders = []
    for item in schedule:
        reminders.append({
            "task": item["task"],
            "reminder": "Daily reminder set"
        })
    return reminders
