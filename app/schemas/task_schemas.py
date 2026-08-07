from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CreateTaskSchema(BaseModel):
    description: str
    deadline: datetime
    # user_id: int

class UpdateTaskSchema(BaseModel):
    description: Optional[str] = None
    deadline: Optional[datetime] = None
