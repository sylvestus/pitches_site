from multiprocessing import managers
from app import create_app,db
import app
from app.models import User,Comments,PhotoProfile,Pitches
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand

# creating app instance
app = create_app('development')
manager = Manager(app)
manager.add_command('server',Server)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
app = create_app('test')
app = create_app('production')

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Pitches = Pitches,Comments = Comments)
if __name__ == '__main__':
    manager.run()
