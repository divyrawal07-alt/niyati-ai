from fastapi import FastAPI
from app.agents.planner_agent import generate_plan
from app.agents.scheduler_agent import create_schedule
from app.agents.reminder_agent import set_reminders
from app.tools.notification_service import send_email_notification

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Niyati AI is running 🚀"}

@app.post("/plan-life")
def plan_life(data: dict):
    priorities = data.get("priorities", {})

    plan = generate_plan(priorities)
    schedule = create_schedule(plan)
    reminders = set_reminders(schedule)

    return {
        "message": "Multi-agent plan generated",
        "plan": plan,
        "schedule": schedule,
        "reminders": reminders
    }
