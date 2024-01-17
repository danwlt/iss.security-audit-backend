from app.utils.PydanticObjectId import PydanticObjectId
from pydantic import BaseModel, Field, StrictBool, EmailStr


class UserModel(BaseModel):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    username: str = Field(...)
    password: str = Field(...)
    active: StrictBool = False
    email: EmailStr = Field(...)
    accessToken: str = Field(...)


class UserPublicModel(BaseModel):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id")
    username: str = Field(...)
    active: StrictBool = False
    email: EmailStr = Field(...)


class NewUser(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
    active: StrictBool = False
    email: EmailStr = Field(...)
