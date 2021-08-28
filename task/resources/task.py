from flask_restful import Resource, reqparse
from task.models import Task as TaskObject


class Tasks(Resource):
    def get(self):
        res = TaskObject.list_tasks()
        if len(res) == 0:
            return {
                "message": "task not exist."
            }, 403
        else:
            result = []
            for task in res:
                result.append({"id": task.id, "name": task.name, "status": task.get_status()})
            return {
                "result": result
            }, 200


class Task(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("name", required=True, help="name is required")

    def post(self):
        # {"name": "買晚餐"}
        arg = self.parser.parse_args()
        name = arg["name"]
        task = TaskObject(name)
        task.create_task()
        return {
            "result": {"name": task.name, "status": task.get_status(), "id": task.id}
        }, 201


class TaskId(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument("name", required=True, help="name is required")
    parser.add_argument("status", required=True, help="status is required")

    def put(self, id):
        # {"name": "買早餐", "status": 1, "id": 1}
        arg = self.parser.parse_args()
        name = arg["name"]
        status = arg["status"]
        task = TaskObject.get_task(id)
        if task is None:
            return {
                "message": "task not exist."
            }, 403
        task.name = name
        task.set_status(int(status))
        task.update_task()
        return {
            "name": task.name,
            "status": task.get_status(),
            "id": task.id
        }, 200

    def delete(self, id):
        task = TaskObject.get_task(id)
        if task is None:
            return {
                "message": "task not exist."
            }, 403
        task.delete_task()
        return {}, 200


class TestCall(Resource):
    def get(self):
        return {
            "message": "Rock'n Roll"
        }, 200
