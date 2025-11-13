from flask import current_app, g
import pyodbc

def get_db():
    if 'db' not in g:
        db_url = current_app.config['pyodbc_conn']
        g.db = pyodbc.connect(db_url)

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)