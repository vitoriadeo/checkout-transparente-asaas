import os
from flask import Flask, render_template
from .config import Prod, Dev, Config
from app.controllers import main

from . import database_manager

def create_app():
    app = Flask(__name__)


    if os.environ.get('FLASK_DEBUG') == '1':
        app.config.from_object(Dev)

    else:
        app.config.from_object(Prod)


    database_manager.init_app(app)


    app.register_blueprint(main.section)


    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return render_template('errors/500.html'), 500
    
    return app