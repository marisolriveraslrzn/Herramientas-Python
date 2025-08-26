import cherrypy
import os

from controllers.task_controller import TaskController

class Root:
    @cherrypy.expose
    def index(self):
        raise cherrypy.HTTPRedirect("/tasks")

if __name__ == '__main__':
    cherrypy.config.update({
        'server.socket_host': '127.0.0.1',
        'server.socket_port': 8080,
        'tools.sessions.on': True,
        'tools.sessions.storage_type': 'ram',
        'tools.staticdir.on': True,
        'tools.staticdir.dir': os.path.abspath('./static'),
        'tools.staticdir.index': 'frontend.html'
    })
    root = Root()
    root.tasks = TaskController()
    cherrypy.quickstart(root)