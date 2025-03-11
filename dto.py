from datetime import datetime
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str
    author: str

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        orm_mode = True