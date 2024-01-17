from pydantic import BaseModel, Field
from pydantic.networks import IPvAnyNetwork
from datetime import date as date_value
from typing import List, Optional
from app.data_models.command_models import Command


class Output(BaseModel):
    output: Optional[str] = Field(...)
    value: Optional[int] = Field(...)


class CommandList(BaseModel):
    command: Command = Field(...)
    result: Output = Field(...)


# Cannot use date as name -> will cause recursion error (https://github.com/pydantic/pydantic/issues/7327)
class Result(BaseModel):
    hostname: str = Field(...)
    ip: IPvAnyNetwork = Field(...)
    date: date_value = Field(...)
    score: int = Field(...)
    commands: List[CommandList] = Field(...)
