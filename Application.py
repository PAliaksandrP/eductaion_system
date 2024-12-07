from fastapi import FastAPI
from view.UserAunteficationView import UserAunteficationView
from view.MainFormView import MainFormView
from view.ChildModeView import ChildModeView
from view.UserInfoView import UserInfoView
from controller.UserAunteficationController import UserAunteficationController
from controller.TaskInfoController import TaskInfoController
from controller.UserInfoController import UserInfoController
from controller.ChildModeController import ChildModeController
import model.data as data


class Application():
    def __init__(self):
        self.app = FastAPI()
        Authcontroller = UserAunteficationController()
        MainController = TaskInfoController()
        user_create = data.User(
            first_name="John",
            last_name="Doe",
            phone_number="+89012332",
            email="j11h3n1.do12e13211122113@example.com",
            enterance_password="secret123",
            child_mode_exit_password="2341"
        )
        ChildmodeController = ChildModeController()
        UserController = UserInfoController(user_create)

        user_router = UserAunteficationView(Authcontroller)
        main_router = MainFormView(MainController)
        child_router = ChildModeView(ChildmodeController)
        edit_router = UserInfoView(UserController)
        self.app.include_router(user_router.router)
        self.app.include_router(main_router.router)
        self.app.include_router(child_router.router)
        self.app.include_router(edit_router.router)