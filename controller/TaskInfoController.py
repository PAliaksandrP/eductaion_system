import model.data as data
import model.crud as crud
import model.database as database


class TaskInfoController:
    def __init__(self):
        self.db = next(database.get_db())

    def __del__(self):
        self.db.close()

    def get_list_tasks(self):
        return crud.get_tasks(self.db)

    def add_task(self, task: data.TaskInfo):
        return crud.create_task(self.db, task)
