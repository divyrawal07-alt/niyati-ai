def create_schedule(plan):
    schedule = []
    for item in plan:
        schedule.append({
            "task": item["task"],
            "daily_time": "2-3 hours"
        })
    return schedule
