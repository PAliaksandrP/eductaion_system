import model.data as data
import model.crud as crud
import model.database as database


class UserInfoController:
    def __init__(self, user: data.User):
        self.db = next(database.get_db())
        self.user = user

    def __del__(self):
        self.db.close()

    def update_password(self, password):
        return crud.update_password(self.db, self.user, password)

    def update_user(self, user: data.UserUpdate):
        return crud.update_user_data(self.db, self.user, user)
