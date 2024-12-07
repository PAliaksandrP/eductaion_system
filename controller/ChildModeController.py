import model.data as data
import model.crud as crud
import model.database as database


class ChildModeController():
    def __init__(self):
        self.db = next(database.get_db())

    def __del__(self):
        self.db.close()

    def get_tasks(self):
        return crud.get_tasks(self.db)

    def exit_child_mode(self, password: str):
        return crud.exit_child(self.db, password)