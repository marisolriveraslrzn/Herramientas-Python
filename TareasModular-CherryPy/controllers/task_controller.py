import cherrypy
from models.task import Task

class TaskController:
    def __init__(self):
        self.tasks = []

    @cherrypy.expose
    def index(self):
        html = "<h2>📋 Lista de tareas</h2><ul>"
        for i, task in enumerate(self.tasks):
            status = "✅" if task.done else "❌"
            html += f"<li>{status} {task.title} <a href='/tasks/toggle?i={i}'>Cambiar</a></li>"
        html += "</ul><form method='post' action='/tasks/add'><input name='title'><button>Agregar</button></form>"
        return html

    @cherrypy.expose
    def add(self, title):
        self.tasks.append(Task(title))
        raise cherrypy.HTTPRedirect("/tasks")

    @cherrypy.expose
    def toggle(self, i):
        i = int(i)
        if 0 <= i < len(self.tasks):
            self.tasks[i].toggle()
        raise cherrypy.HTTPRedirect("/tasks")
