from pydantic import BaseModel, Json


class NumberAdd(BaseModel):
    id: int
    numbers:  dict

class MessageAdd(BaseModel):
    id: int
    messages: str
    numbers:  dict