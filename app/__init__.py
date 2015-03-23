import os
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()
lm = LoginManager()
lm.login_view = 'main.login'


def create_app(config_name):
    """Crear una instancia de l'aplicacio"""
    app = Flask(__name__)

    #Importar configuracio en funcio del tipus de aplicacio (dev...)
    cfg = os.path.join(os.getcwd(), 'config', config_name + '.py')
    app.config.from_pyfile(cfg)

    #Inicialitzar extensions
    bootstrap.init_app(app)
    db.init_app(app)
    lm.init_app(app)

    #Importar blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #configure production logging of errors
    if not app.config['DEBUG'] and not app.config['TESTING']:
        import logging
        from logging.handlers import SMTPHandler
        mail_handler = SMTPHandler('127.0.0.1', 'error@example.com',
                                   app.config['ADMINS'], 'Application Error')
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    return app





