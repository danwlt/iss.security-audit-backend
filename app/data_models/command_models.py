from pydantic import BaseModel, Field
from typing import List

# ToDo - Add Weight


class Command(BaseModel):
    chapter: str = Field(...)
    description: str = Field(...)
    command: str = Field(...)
    level: List[int] = Field(...)
    weight: int = Field(...)
