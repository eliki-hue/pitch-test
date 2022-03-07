from app import myapp, db
from flask_script import Manager, Server
from flask_migrate import Migrate
from app.models import User, Pitch


# app = initializer('development')

manager = Manager(myapp)
manager.add_command('server', Server)
@manager.command
def test():
    '''Run the unit tests'''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

migrate = Migrate(myapp,db)
manager.add_command('db', Migrate)

@manager.shell
def make_shell_context():
    return dict(myapp = myapp,db = db,User = User, Pitch = Pitch )

if __name__ == '__main__':
    manager.run()
