from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, JSON


metadata = MetaData()

user = Table(
    "user", 
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
    Column("email", String, nullable=False),
    Column("password", String, nullable=False),
    Column("numbers_id", Integer, ForeignKey("number.id"))
)

number = Table(
    "number", 
    metadata,
    Column("id", Integer, primary_key=True),
    Column("numbers", JSON)
    
)