import os

import sqlalchemy
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from task.models import db
from task.resources.task import Task, TaskId, Tasks, TestCall

# Load environment variables
load_dotenv()
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_PORT = os.getenv('MYSQL_PORT')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{}:{}@{}:{}/{}".format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True

db.init_app(app)
migrate = Migrate(app, db)

api.add_resource(TestCall, '/hehe')
api.add_resource(Tasks, "/tasks")
api.add_resource(Task, "/task")
api.add_resource(TaskId, "/task/<int:id>")

@app.route("/")
def hello():
    return "Rock'n Roll"

@app.route('/test')
def index():

    sql_cmd = """
        select *
        from tasks
        """

    query_data =  db.session.execute(sqlalchemy.text(sql_cmd))
    print(query_data)
    return 'ok'

if __name__ == "__main__":
    app.run()
