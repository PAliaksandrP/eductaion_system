from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import model.data as data
from controller.UserAunteficationController import UserAunteficationController


class UserAunteficationView():
    def __init__(self, controller: UserAunteficationController):
        self.router = APIRouter()
        self._add_routes()
        self.templates = Jinja2Templates(directory="view/templates")
        self.controller = controller
    def _add_routes(self):
        @self.router.get("/", response_class=HTMLResponse)
        async def home(request: Request):
            return self.templates.TemplateResponse("register_login.html", {"request": request})

        @self.router.post("/login")
        async def login(email: str = Form(...), password: str = Form(...)):
            login = data.UserCheck(email=email, enterance_password=password)
            print(login)
            result = self.controller.check_user_input(login)
            if result is None:
                return RedirectResponse(url="/", status_code=302)
            else:
                return RedirectResponse(url="/main/", status_code=302)
        #{"message": "Logged in", "username": username}

        @self.router.post("/register")
        async def register(first_name: str = Form(...), last_name: str = Form(...), email: str = Form(...),
                           phone: str = Form(...), password: str = Form(...), child_password: str = Form(...)):
            user = data.User(first_name=first_name, last_name=last_name,
                             email=email, enterance_password=password,
                             child_mode_exit_password=child_password, phone_number=phone)
            self.controller.register_user_input(user)
            return RedirectResponse(url="/", status_code=302)
