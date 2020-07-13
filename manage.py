# import Flask Script object
#from flask.ext.script import Manager, Server
import os
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from qianblog import create_app
from qianblog import models

# Get the ENV from os_environ
env = os.environ.get('BLOG_ENV', 'dev')
# Create thr app instance via Factory Method
app = create_app('qianblog.config.%sConfig' % env.capitalize())


# Init manager object via app object
manager = Manager(app)

# Init migrate object via app and db object
migrate = Migrate(app, models.db)

# Create some new commands
manager.add_command("server", Server(host='10.0.0.8', port=9999))
manager.add_command("db", MigrateCommand)


@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    # 确保有导入 Flask app object，否则启动的 CLI 上下文中仍然没有 app 对象
    return dict(app=app,
                db=models.db,
                User=models.User,
                Post=models.Post,
                Comment=models.Comment,
                Tag=models.Tag,
                Server=Server,
                Role=models.Role)


if __name__ == '__main__':
    manager.run()

