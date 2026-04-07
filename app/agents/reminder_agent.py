def set_reminders(schedule):
    reminders = []
    for item in schedule:
        reminders.append({
            "task": item["task"],
            "reminder_time": "9:00 AM",
            "status": "Scheduled",
            "integration": "Can be synced with Google Calendar"
        })
    return reminders
