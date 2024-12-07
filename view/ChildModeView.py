from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import model.data as data
from controller.ChildModeController import ChildModeController


class ChildModeView():
    def __init__(self, controller: ChildModeController):
        self.router = APIRouter()
        self._add_routes()
        self.templates = Jinja2Templates(directory="view/templates")
        self.controller = controller
    def _add_routes(self):
        @self.router.get("/child-mode")
        def get_child_mode(request: Request):
            items = [
                data.TaskInfo(type="Название 1", difficulty=2,  task_info="Описание 1"),
                data.TaskInfo(type="Название 2", difficulty=4,  task_info="Описание 2"),
            ]
            return self.templates.TemplateResponse("child_mode.html", {"request": request, "items": items})

        @self.router.get("/logout", response_class=HTMLResponse)
        async def logout(request: Request):
            return self.templates.TemplateResponse("exit_child.html", {"request": request})
        @self.router.post("/exit-child-mode")
        async def exit_child_mode(exit_code: str = Form(...)):
            if self.controller.exit_child_mode(exit_code):
                return RedirectResponse(url="/main", status_code=302)
            else:
                return RedirectResponse(url="child-mode", status_code=302)