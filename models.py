from pydantic import BaseModel, Field


class Post(BaseModel):
    user_id: int = Field(alias='id')
    post_id: int = Field(alias='id')
    title: str
    body: str
