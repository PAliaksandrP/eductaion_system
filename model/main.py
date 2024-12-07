from sqlalchemy.orm import Session
import crud, table, data, database

# Функция для получения сессии

db = next(database.get_db())



# Создание таблиц в базе данных
table.Base.metadata.create_all(bind=database.engine)
user = data.User(
    first_name="John",
    last_name="Doe",
    phone_number="+89012332",
    email="j1h3n1.do12e23513211122113@example.com",
    enterance_password="secret123",
    child_mode_exit_password="2341"
)

crud.create_task(db,data.TaskInfo(type="Название 1", difficulty=2, task_info="Описание 1"))
crud.create_task(db,data.TaskInfo(type="Название 2", difficulty=4, task_info="Описание 2"))

crud.create_user(db=db, user=user)
user = crud.get_users(db=db)
check = data.UserCheck(email="j1h3n.do12e132122113@example.com",
                       enterance_password="secret123")
res = crud.check_user(db, check)
print(res)
db.close()