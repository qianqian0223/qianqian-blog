from flask import Flask
from config import DevConfig
import wt_forms

app = Flask(__name__)

# Get the config from object of DecConfig
# 使用 onfig.from_object() 而不使用 app.config['DEBUG'] 是因为这样可以加载 class DevConfig 的配置变量集合，而不需要一项一项的添加和修改。
app.config.from_object(DevConfig)


# Import the views module
views = __import__('views')



if __name__ == '__main__':
    # Entry the application 
    app.run()

