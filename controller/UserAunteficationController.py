import model.data as data
import model.crud as crud
import model.database as database


class UserAunteficationController:
    def __init__(self):
        self.db = next(database.get_db())

    def __del__(self):
        self.db.close()

    def check_user_input(self, user_input: data.UserCheck):
        print("Fuck")
        return crud.check_user(self.db, user_input)

    def register_user_input(self, user_input: data.User):
        return crud.create_user(self.db, user_input)


if __name__ == "__main__":
    user = UserAunteficationController()
    check = data.UserCheck(email="j1h3n.do12e132122113@example.com",
    enterance_password="secret123")


    res = user.check_user_input(check)
    print(res)