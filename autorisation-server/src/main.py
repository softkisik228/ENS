from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from fastapi import Depends

from auth.auth import auth_backend
from database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

app = FastAPI()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

# current_user = fastapi_users.current_user()

# @app.get("/protected-route")
# async def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.email}"

# @app.get("/unprotected-route")
# async def unprotected_route():
#     return f"Hello, anonym"