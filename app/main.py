from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Niyati AI is running 🚀"}

@app.post("/plan-life")
def plan_life(data: dict):
    return {
        "message": "Plan generated successfully",
        "input": data
    }
