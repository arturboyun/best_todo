from typing import List as TList

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    list_id: int

    class Config:
        orm_mode = True


class ListBase(BaseModel):
    title: str


class ListCreate(ListBase):
    pass


class List(ListBase):
    id: int
    owner_id: int
    items: TList[Item] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    lists: TList[List] = []

    class Config:
        orm_mode = True
