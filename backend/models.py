# models.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class Achievement(BaseModel):
    id: int
    title: str
    description: str
    icon_url: str
    earned: bool = False
    earned_date: Optional[date] = None
    progress: Optional[int] = None
    required: Optional[int] = None

class Badge(BaseModel):
    id: int
    title: str
    description: str
    icon_url: str
    criteria: List[int]
    earned: bool = False
    earned_date: Optional[str] = None

class User(BaseModel):
    id: int
    name: str
    avatar: str

class AchievementEarnRequest(BaseModel):
    user_id: int
    achievement_id: int
