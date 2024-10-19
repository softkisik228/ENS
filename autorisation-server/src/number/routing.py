from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_async_session
from .models.models import number, message

router = APIRouter(
    prefix="/numbers",
    tags=["Numbers"]
)


@router.get("/get_numbers")
async def get_numbers(number_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(message).where(message.c.id == number_id)
    result = await session.execute(query)
    num = result.fetchone()

    if num is None:
        raise HTTPException(status_code=404, detail="Number not found")
    return {"id": num.id, "numbers": num.numbers}

@router.get("/get_messages")
async def get_numbers(message_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(message).where(number.c.id == message_id)
    result = await session.execute(query)
    mes = result.fetchone()
    
    if mes is None:
        raise HTTPException(status_code=404, detail="Messages not found")
    return {"id": mes.id,"messages": mes.messages, "numbers": mes.numbers}


@router.post("/add_numbers")
async def add_numbers():
    return {"Num": "hrum"}
