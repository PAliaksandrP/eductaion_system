from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Модель для Child
class Child(Base):
    __tablename__ = "children"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    age = Column(Integer)

# Модель для TaskInfo
class TaskInfo(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    difficulty = Column(Integer)
    task_info = Column(String)

# Модель для User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    email = Column(String, unique=True, index=True)
    enterance_password = Column(String)
    child_mode_exit_password = Column(String)
