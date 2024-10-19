from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_async_session
from .models.models import number

router = APIRouter(
    prefix="/numbers",
    tags=["Numbers"]
)


@router.get("/get_numbers")
async def get_numbers(number_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(number).where(number.c.id == number_id)
    result = await session.execute(query)
    num = result.fetchone()
    
    if num is None:
        raise HTTPException(status_code=404, detail="Number not found")
    return {"id": num.id, "numbers": num.numbers}

@router.post("/add_numbers")
async def add_numbers():
    return {"Num": "hrum"}
