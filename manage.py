from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Post


#Creating app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

#Tests
@manager.command
def test():
    """
    Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=5).run(tests) 

#To access it, run '$python3'
@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Post = Post )
if __name__ == '__main__':
    manager.run()