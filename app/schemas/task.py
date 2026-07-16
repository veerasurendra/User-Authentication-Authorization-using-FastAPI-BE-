from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict

from app.models.task import TaskStatus, TaskPriority


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200, examples=["Buy groceries"])
    description: str | None = Field(None, max_length=2000)
    status: TaskStatus = TaskStatus.pending
    priority: TaskPriority = TaskPriority.medium


class TaskCreate(TaskBase):
    """Payload for POST /tasks"""
    pass


class TaskUpdate(BaseModel):
    """Payload for PUT /tasks/{id} - all fields optional (partial update)."""
    title: str | None = Field(None, min_length=1, max_length=200)
    description: str | None = Field(None, max_length=2000)
    status: TaskStatus | None = None
    priority: TaskPriority | None = None


class TaskOut(TaskBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime
