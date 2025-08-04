from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from data import users, badges, achievements 
import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AchievementEarnRequest(BaseModel):
    user_id: int
    achievement_id: int

@app.get("/api/users/{user_id}/achievements")
def get_user_achievements(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "user": users[user_id],
        "achievements": achievements
    }

@app.get("/api/users/{user_id}/badges")
def get_user_badges(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    user_achievements = {a.id for a in achievements if a.earned}
    for badge in badges:
        if set(badge.criteria).issubset(user_achievements):
            badge.earned = True
            if not badge.earned_date:
                badge.earned_date = str(datetime.date.today())
        else:
            badge.earned = False
            badge.earned_date = None

    return {
        "user": users[user_id],
        "badges": badges
    }

@app.post("/api/achievements/earn")
def earn_achievement(data: AchievementEarnRequest):
    found = False
    for a in achievements:
        if a.id == data.achievement_id:
            if a.earned:
                return {"message": "Already earned"}
            a.earned = True
            a.earned_date = str(datetime.date.today())
            found = True
            break

    if not found:
        raise HTTPException(status_code=404, detail="Achievement not found")

    return {"message": f"Achievement {data.achievement_id} marked as earned"}

@app.post("/api/users/{user_id}/achievements/increament/{ach_id}")
def increment_achievement(user_id: int, ach_id: int):
    for ach in achievements:
        if ach.id == ach_id:
            if ach.earned:
                return {"message": "Already earned", "progress": ach.progress}

            ach.progress += 1
            if ach.progress >= ach.required:
                ach.earned = True
                ach.earned_date = str(datetime.date.today())

            return {
                "message": "Progress updated",
                "progress": ach.progress,
                "earned": ach.earned
            }

    raise HTTPException(status_code=404, detail="Achievement not found")

