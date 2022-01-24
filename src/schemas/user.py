from pydantic import BaseModel, Field, validator


class UserSchema(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    birth_date: str = Field(...)
    phone: str = Field(...)
    password: str = Field(...)

    class Config:
        orm_mode = True


class UserLoginSchema(BaseModel):
    phone: str = Field(...)
    password: str = Field(...)


class UserLoginOTPSchema(BaseModel):
    phone: str = Field(...)

    @validator('phone')
    def check_phone(cls, v):
        if not v.isdigit():
            raise ValueError('Phone number must be numeric')
        if len(v) != 10:
            raise ValueError('Phone number must be 10 digits')
        return v


class UserLoginOTPConfirmSchema(BaseModel):
    phone: str = Field(...)
    code: str = Field(...)

    @validator('phone')
    def check_phone(cls, v):
        if not v.isdigit():
            raise ValueError('Phone number must be numeric')
        if len(v) != 10:
            raise ValueError('Phone number must be 10 digits')
        return v

    @validator('code')
    def check_code(cls, v):
        if not v.isdigit():
            raise ValueError('Code must be numeric')
        if len(v) != 4:
            raise ValueError('Code must be 4 digits')
        return v
