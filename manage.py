from app import initializer, db
from flask_script import Manager, Server


app = initializer('development')

manager = Manager(app)
manager.add_command('server', Server)
