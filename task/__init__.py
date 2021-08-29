from flask import Flask
from flask_restful import Api

from task.resources.task import Task, TaskId, Tasks, TestCall

from .config.config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    api = Api(app)
    api.add_resource(TestCall, '/hehe')
    api.add_resource(Tasks, "/tasks")
    api.add_resource(Task, "/task")
    api.add_resource(TaskId, "/task/<int:id>")
    return app
