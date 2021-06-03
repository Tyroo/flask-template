from flask import Flask
from app import views
from configure import settings


def create_app():
    # 实例化一个Flask对象
    app = Flask(__name__)
    # 加载Flask配置
    app.config.from_object(settings)
    # 注册蓝图
    views.register_bp(app=app)

    return app
