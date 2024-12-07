from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from controller.TaskInfoController import TaskInfoController
import model.data as data

class MainFormView():
    def __init__(self, controller: TaskInfoController):
        self.router = APIRouter()
        self._add_routes()
        self.templates = Jinja2Templates(directory="view/templates")
        self.controller = controller

    def _add_routes(self):
        @self.router.get("/main/")
        async def main(request: Request):
            ages = [3, 4, 5, 6, 7]
            skills = ["Чтение", "Математика", "Творчество"]
            items = self.controller.get_list_tasks()
            ages = [3, 4, 5, 6, 7]
            skills = ["Чтение", "Математика", "Творчество"]
            return self.templates.TemplateResponse("main.html", {"request": request,
                "items": items,
                "ages": ages,
                "skills": skills})