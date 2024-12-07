from sqlalchemy.orm import Session
import model.table as table
import model.data as data
from sqlalchemy import and_

def create_child(db: Session, child: data.Child):
    db_child = table.Child(first_name=child.first_name, age=child.age)
    db.add(db_child)
    db.commit()
    db.refresh(db_child)
    return db_child

def get_children(db: Session, skip: int = 0, limit: int = 100):
    return db.query(table.Child).offset(skip).limit(limit).all()

# CRUD для TaskInfo
def create_task(db: Session, task: data.TaskInfo):
    db_task = table.TaskInfo(type=task.type, difficulty=task.difficulty, task_info=task.task_info)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    tasks = db.query(table.TaskInfo).offset(skip).limit(limit).all()
    tasks_list = [data.TaskInfo.from_orm(task) for task in tasks]
    return tasks_list
# CRUD для User
def create_user(db: Session, user: data.User):
    db_user = table.User(first_name=user.first_name, last_name=user.last_name,
                          phone_number=user.phone_number, email=user.email,
                          enterance_password=user.enterance_password,
                          child_mode_exit_password=user.child_mode_exit_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    users = db.query(table.User).offset(skip).limit(limit).all()
    # Преобразуем каждый объект User в Pydantic с использованием from_orm
    users_list = [data.User.from_orm(user) for user in users]
    return users_list


def check_user(db: Session, user: data.UserCheck):
    user = db.query(table.User).filter(and_(table.User.email == user.email,table.User.enterance_password== user.enterance_password)).first()
    return data.User.from_orm(user) if user else None


def exit_child(db: Session, password: str):
    user = db.query(table.User).filter(and_(table.User.child_mode_exit_password == password)).first()
    return True if user else False


def update_user_data(db: Session, user_old: data.User, user_update: data.User):
    user = db.query(table.User).filter(and_(table.User.email == user_old.email)).first()
    if not user:
        return None  # Пользователь не найден
    for key, value in user_update.dict(exclude_unset=True).items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return data.User.from_orm(user)


def update_password(db: Session, user_old: data.User, password: str):
    user = db.query(table.User).filter(and_(table.User.email == user_old.email)).first()
    if not user:
        return None  # Пользователь не найден
    user.enterance_password = password
    db.commit()
    db.refresh(user)
    return data.User.from_orm(user)
