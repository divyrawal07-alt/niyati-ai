def generate_plan(priorities):
    plan = []
    for task, percent in priorities.items():
        hours = (percent / 100) * 7 * 4
        plan.append({
            "task": task,
            "weekly_hours": round(hours, 2)
        })
    return plan
