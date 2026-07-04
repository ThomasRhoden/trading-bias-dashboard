from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='views/templates')
    from app.controllers.main_controller import main_blueprint
    app.register_blueprint(main_blueprint)
    return app