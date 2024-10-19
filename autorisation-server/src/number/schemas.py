from pydantic import BaseModel, Json


class NumberAdd(BaseModel):
    id: int
    numbers:  dict