from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '__fsj_key__'
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from analyse_data import models, views, api_1_0

from flask_bootstrap import Bootstrap

bootstrap=Bootstrap(app)

if __name__ == '__main__':
    for i in dict(app.config).items():
        print(i)
    print(app.view_functions)
