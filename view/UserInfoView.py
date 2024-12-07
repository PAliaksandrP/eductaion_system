from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import model.data as data
from controller.UserInfoController import UserInfoController



class UserInfoView():
    def __init__(self, controller: UserInfoController):
        self.router = APIRouter()
        self._add_routes()
        self.templates = Jinja2Templates(directory="view/templates")
        self.controller = controller

    def _add_routes(self):
        @self.router.get("/edit_user", response_class=HTMLResponse)
        async def home(request: Request):
            return self.templates.TemplateResponse("edit_user.html", {"request": request})
        @self.router.post("/update_user")
        async def update_user(first_name: str = Form(...), last_name: str = Form(...),
                              email: str = Form(...), phone: str = Form(...), enterance_password: str = Form(...),
                              child_password: str = Form(...)):
            new = data.User(first_name=first_name, last_name=last_name, email=email, enterance_password=enterance_password,
                       child_mode_exit_password=child_password, phone_number=phone)
            return RedirectResponse(url="/main", status_code=302)