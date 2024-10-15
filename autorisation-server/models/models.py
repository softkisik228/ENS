from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, JSON, Boolean


metadata = MetaData()

user = Table(
    "user", 
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
    Column("email", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("numbers_id", Integer, ForeignKey("number.id")),
    Column("is_active", Boolean),
    Column("is_superuser", Boolean),
    Column("is_verified", Boolean)

)

number = Table(
    "number", 
    metadata,
    Column("id", Integer, primary_key=True),
    Column("numbers", JSON)
    
)