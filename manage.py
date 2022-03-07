from app import initializer, db
from flask_script import Manager, Server
from flask_migrate import Migrate


app = initializer('development')

manager = Manager(app)
manager.add_command('server', Server)
@manager.command
def test():
    '''Run the unit tests'''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

migrate = Migrate(app,db)
manager.add_command('db', Migrate)

@manager.shell
