from app import  db, app
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Pitch





manager = Manager(app)
manager.add_command('server', Server)
@manager.command
def test():
    '''Run the unit tests'''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

migrate = Migrate()
migrate.init_app(app, db)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Pitch = Pitch )

if __name__ == '__main__':
    manager.run()


