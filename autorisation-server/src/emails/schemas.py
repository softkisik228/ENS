from pydantic import BaseModel


class EmailAdd(BaseModel):
    id: int
    emails: dict

class MessageAdd(BaseModel):
    id: int
    messages: str
    emails: dict

class MessageToSend(BaseModel):
    message: str
    emails: dict
