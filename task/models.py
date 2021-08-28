from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Boolean, default=False)

    def __init__(self, name, status=0):
        self.name = name
        self.status = True if status else False

    def set_status(self, status):
        self.status = True if status else False

    def get_status(self):
        return 1 if self.status else 0

    def create_task(self):
        db.session.add(self)
        db.session.commit()

    def delete_task(self):
        db.session.delete(self)
        db.session.commit()

    def update_task(self):
        db.session.commit()

    @classmethod
    def get_task(cls, id):
        return cls.query.get(id)

    @classmethod
    def list_tasks(cls):
        return cls.query.all()
