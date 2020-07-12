from flask import Flask, redirect,url_for

from .config import DevConfig
from .models import db
from qianblog.controllers import blog



app = Flask(__name__)

# Get the config from object of DecConfig
# 使用 onfig.from_object() 而不使用 app.config['DEBUG'] 是因为这样可以加载 class DevConfig 的配置变量集合，而不需要一项一项的添加和修改。
app.config.from_object(DevConfig)

# Will be load the SQLALCHEMY_DATABASE_URL from config.py to db object
db.init_app(app)

@app.route('/')
def index():
    # Redirect the Request_url '/' to '/blog/'
    return redirect(url_for('blog.home'))

# Register the Blueprint into app object
app.register_blueprint(blog.blog_blueprint)

if __name__ == '__main__':
    app.run()


