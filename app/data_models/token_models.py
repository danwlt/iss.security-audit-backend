from pydantic import BaseModel, Field


class TokenDataModel(BaseModel):
    username: str = Field(...)


class TokenModel(BaseModel):
    access_token: str = Field(...)
    token_type: str = Field(...)
    data: TokenDataModel = Field(...)
