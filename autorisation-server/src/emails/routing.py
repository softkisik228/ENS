from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, delete

from database import get_async_session
from .models.models import email, message
from .schemas import EmailAdd, MessageAdd, MessageToSend
from .sms_sender import send_email_notification

router = APIRouter(
    prefix="/emails",
    tags=["Emails"]
)


@router.get("/get_emails")
async def get_emails(email_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(email).where(email.c.id == email_id)
    result = await session.execute(query)
    em = result.fetchone()

    if em is None:
        raise HTTPException(status_code=404, detail="Email not found")
    return {"id": em.id, "emails": em.emails}

@router.get("/get_messages")
async def get_messages(message_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(message).where(message.c.id == message_id)
    result = await session.execute(query)
    mes = result.fetchall()
    
    if mes is None:
        raise HTTPException(status_code=404, detail="Messages not found")
    return [{"id": mes.id,"messages": mes.messages, "emails": mes.emails} for mes in mes]

@router.post("/add_emails")
async def add_emails(new_emails: EmailAdd, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(email).where(email.c.id == new_emails.model_dump()["id"])
        result = await session.execute(query)
        em = result.fetchone()
        if em == None:
            stmnt = insert(email).values(new_emails.model_dump())
            await session.execute(stmnt)
            await session.commit()
        else:
            combined = {**em.emails, **new_emails.model_dump()['numbers']}
            stmt = (
            update(email)
            .where(email.c.id == new_emails.model_dump()["id"])
            .values(numbers=combined)
            )
            await session.execute(stmt)
            await session.commit()
    except Exception as e:
        print(e)
        return e
    return new_emails



@router.post("/add_message")
async def add_message(new_message: MessageAdd, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(message).where(message.c.id == new_message.model_dump()["id"])
        result = await session.execute(query)
        mes = result.fetchone()
        if mes == None:
            stmnt = insert(message).values(new_message.model_dump())
            await session.execute(stmnt)
            await session.commit()
        elif mes.messages == new_message.model_dump()["messages"]:
            combined = {**mes.emails, **new_message.model_dump()["emails"]}
            stmt = (
            update(message)
            .where(message.c.id == new_message.model_dump()["id"])
            .values(emails=combined)
            )
            await session.execute(stmt)
            await session.commit()
        else:
            stmnt = insert(message).values(new_message.model_dump())
            await session.execute(stmnt)
            await session.commit()
    except Exception as e:
        print(e)
        return e
    return new_message

@router.post("/del_message")
async def delite_message(id: int, message_to_del: str, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(message).where((message.c.id == id) & (message.c.messages == message_to_del))
    await session.execute(stmt)
    await session.commit()
    return {"status": "ok"}

@router.post("/send_message")
async def send_message(message_to_send: MessageToSend, session: AsyncSession = Depends(get_async_session)):
    try:
        message_to_send = message_to_send.model_dump()
        for email in message_to_send["emails"].values():
            print(email)
            send_email_notification.delay(message_to_send["message"], email)
    except Exception as e:
        print(e)
        return e
    return {"status": "ok"}
