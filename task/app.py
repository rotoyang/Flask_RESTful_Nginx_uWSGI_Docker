from flask_migrate import Migrate

from task import create_app
from task.models import db


app = create_app("development")
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    return "Rock'n Roll"


if __name__ == "__main__":
    app.run()


@app.cli.command()
def test():
    import sys
    import unittest

    tests = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.errors or result.failures:
        sys.exit(1)
