from pydantic import BaseModel
from typing import Optional

class Child(BaseModel):
    first_name: str
    age: int

    class Config:
        from_attributes = True  # Это нужно для преобразования модели в Pydantic


class TaskInfo(BaseModel):
    type: str
    difficulty: int
    task_info: str

    class Config:
        from_attributes = True  # Это нужно для преобразования модели в Pydantic


class User(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    enterance_password: str
    child_mode_exit_password: str

    class Config:
        from_attributes = True  # Это нужно для преобразования модели в Pydantic


class UserCheck(BaseModel):
    email: str
    enterance_password: str

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    enterance_password: Optional[str] = None
    child_mode_exit_password: Optional[str] = None
