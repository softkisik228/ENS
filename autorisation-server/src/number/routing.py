from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, delete

from database import get_async_session
from .models.models import number, message
from .schemas import NumberAdd, MessageAdd

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

@router.get("/get_messages")
async def get_numbers(message_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(message).where(number.c.id == message_id)
    result = await session.execute(query)
    mes = result.fetchone()
    
    if mes is None:
        raise HTTPException(status_code=404, detail="Messages not found")
    return {"id": mes.id,"messages": mes.messages, "numbers": mes.numbers}


@router.post("/add_numbers")
async def add_numbers(new_numbers: NumberAdd, session: AsyncSession = Depends(get_async_session)):
    query = select(number).where(number.c.id == new_numbers.model_dump()["id"])
    result = await session.execute(query)
    num = result.fetchone()
    if num == None:
        stmnt = insert(number).values(new_numbers)
        await session.execute(stmnt)
        await session.commit()
    else:
        combined = {**num.numbers, **new_numbers.model_dump()['numbers']}
        stmt = (
        update(number)
        .where(number.c.id == new_numbers.model_dump()["id"])
        .values(numbers=combined)
        )
        await session.execute(stmt)
        await session.commit()
    return new_numbers

@router.post("/add_message")
async def add_numbers(new_message: MessageAdd, session: AsyncSession = Depends(get_async_session)):
    query = select(message).where(message.c.id == new_message.model_dump()["id"])
    result = await session.execute(query)
    mes = result.fetchone()
    if mes == None:
        stmnt = insert(message).values(new_message.model_dump())
        await session.execute(stmnt)
        await session.commit()
    elif mes.messages == new_message.model_dump()["messages"]:
        combined = {**mes.numbers, **new_message.model_dump()["numbers"]}
        stmt = (
        update(message)
        .where(message.c.id == new_message.model_dump()["id"])
        .values(numbers=combined)
        )
        await session.execute(stmt)
        await session.commit()
    else:
        stmnt = insert(message).values(new_message.model_dump())
        await session.execute(stmnt)
        await session.commit()
    return new_message

@router.post("/del_message")
async def delite_message(id: int, message_to_del: str, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(message).where((message.c.id == id) & (message.c.messages == message_to_del))
    await session.execute(stmt)
    await session.commit()
    return {"status": "ok"}