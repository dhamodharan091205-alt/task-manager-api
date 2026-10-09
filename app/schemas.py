from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserResponse(BaseModel):
    id: int
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TaskCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(default="", max_length=1000)
    status: Literal["pending", "in_progress", "completed"] = "pending"
    priority: Literal["low", "medium", "high"] = "medium"
    due_date: datetime | None = None


class TaskUpdate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(default="", max_length=1000)
    status: Literal["pending", "in_progress", "completed"]
    priority: Literal["low", "medium", "high"]
    due_date: datetime | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str
    priority: str
    due_date: datetime | None
    created_at: datetime
    owner_id: int

    model_config = ConfigDict(from_attributes=True)