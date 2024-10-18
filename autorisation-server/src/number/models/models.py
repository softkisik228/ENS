from sqlalchemy import MetaData, Table, Column, Integer, String, JSON, Boolean


metadata = MetaData()

number = Table(
    "number", 
    metadata,
    Column("id", Integer),
    Column("numbers", JSON)
    
)

message = Table(
    "message", 
    metadata,
    Column("id", Integer),
    Column("messages", String),
    Column("numbers", JSON)
    
)