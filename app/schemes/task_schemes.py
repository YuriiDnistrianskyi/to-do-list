from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CreateTaskScheme(BaseModel):
    description: str
    deadline: datetime
    # user_id: int

class UpdateTaskScheme(BaseModel):
    description: Optional[str] = None
    deadline: Optional[datetime] = None
