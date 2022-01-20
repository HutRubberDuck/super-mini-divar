from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)


class UserLoginSchema(BaseModel):
    email: str = Field(...)
    password: str = Field(...)
