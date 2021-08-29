import unittest

from flask_testing import TestCase
from task import create_app
from task.models import db


class SettingBase(TestCase):
    def create_app(self):
        app = create_app("testing")
        db.init_app(app)
        return app
    
    def setUp(self):
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()


class CheckListTasks(SettingBase):
    def test_list_tasks_no_tasks_403(self):
        response = self.client.get("/tasks")
        self.assertEqual(response.status_code, 403)
    
    def test_list_tasks_200(self):
        self.client.post("/task", json={"name": "買早餐"})
        response = self.client.get("/tasks")
        self.assertEqual(response.status_code, 200)


class CheckCreateTask(SettingBase):
    def test_create_task_201(self):
        response = self.client.post("/task", json={"name": "買早餐"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"result": {"name": "買早餐", "status": 0, "id": 1}})
    
    def test_create_task_no_name_400(self):
        response = self.client.post("/task", json={})
        self.assertEqual(response.status_code, 400)


class CheckUpdateTask(SettingBase):
    def test_update_task_200(self):
        self.client.post("/task", json={"name": "買早餐"})
        response = self.client.put("/task/1", json={"name": "買早餐", "status": 1, "id": 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"name": "買早餐", "status": 1, "id": 1})

    def test_update_task_no_id_200(self):
        self.client.post("/task", json={"name": "買早餐"})
        response = self.client.put("/task/1", json={"name": "買早餐", "status": 1})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"name": "買早餐", "status": 1, "id": 1})
    
    def test_update_task_no_name_400(self):
        response = self.client.put("/task/1", json={"status": 1, "id": 1})
        self.assertEqual(response.status_code, 400)
    
    def test_update_task_no_status_400(self):
        response = self.client.put("/task/1", json={"name": "買早餐"})
        self.assertEqual(response.status_code, 400)
    
    def test_update_task_no_body_400(self):
        response = self.client.put("/task/1", json={})
        self.assertEqual(response.status_code, 400)
        
    def test_update_task_no_arg_id_404(self):
        response = self.client.put("/task/", json={})
        self.assertEqual(response.status_code, 404)


class CheckDeleteTask(SettingBase):
    def test_delete_task_200(self):
        self.client.post("/task", json={"name": "買早餐"})
        response = self.client.delete("/task/1")
        self.assertEqual(response.status_code, 200)
        
    def test_delete_task_no_task_403(self):
        response = self.client.delete("/task/1")
        self.assertEqual(response.status_code, 403)
        
    def test_delete_task_no_arg_id_404(self):
        response = self.client.delete("/task/")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
