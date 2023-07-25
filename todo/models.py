import datetime

from pydantic import BaseModel, Field, field_validator


class ActiveTask(BaseModel):
    task: str = Field(alias="content")
    priority: int
    labels: list
    due: str

    @field_validator("due", mode="before")
    def cast_date(v):
        return v["date"]
        # return datetime.datetime.strptime(v["date"], "%Y-%m-%d")
