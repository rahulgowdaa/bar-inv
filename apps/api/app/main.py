from collections.abc import Awaitable, Callable
from typing import Annotated, Literal

from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Bar Inventory API", version="0.1.0")

Role = Literal["Admin", "Manager", "Staff"]


class UserCtx(BaseModel):
    user_id: int
    org_id: int
    outlet_id: int | None
    role: Role
    email: str


async def get_current_user() -> UserCtx:
    return UserCtx(user_id=1, org_id=1, outlet_id=1, role="Staff", email="demo@example.com")


UserDep = Annotated[UserCtx, Depends(get_current_user)]


def require_role(*allowed: Role) -> Callable[[UserDep], Awaitable[UserCtx]]:
    async def guard(user: UserDep) -> UserCtx:
        if user.role not in allowed:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")
        return user

    return guard


@app.get("/me")
async def me(user: UserDep) -> UserCtx:
    return user


class LoginReq(BaseModel):
    email: str
    password: str


@app.post("/auth/login")
async def login(_: LoginReq) -> dict[str, str]:
    return {"access_token": "stub", "token_type": "bearer"}
