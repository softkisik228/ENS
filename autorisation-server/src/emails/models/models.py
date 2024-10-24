from sqlalchemy import MetaData, Table, Column, Integer, String, JSON, Boolean


metadata = MetaData()

email = Table(
    "email", 
    metadata,
    Column("id", Integer),
    Column("emails", JSON)
    
)

message = Table(
    "message", 
    metadata,
    Column("id", Integer),
    Column("messages", String),
    Column("emails", JSON)
    
)