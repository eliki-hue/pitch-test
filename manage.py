from app import  db, app
from flask_script import Manager, Server
# from flask_migrate import Migrate
from app.models import User, Pitch




manager = Manager(app)
manager.add_command('server', Server)
# @manager.command
# def test():
#     '''Run the unit tests'''
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)

# migrate = Migrate(app,db)
# manager.add_command('db', Migrate)

# @manager.shell
# def make_shell_context():
#     return dict(app = app,db = db,User = User, Pitch = Pitch )

if __name__ == '__main__':
    manager.run()


# from flask_script import Manager, Server
# from app import app



# manager = Manager(app)
# manager.add_command('server', Server)

# if __name__=='__main__':
#     manager.run()